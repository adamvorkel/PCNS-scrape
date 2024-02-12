# pip install aiohttp[speedups]
import os
import sys
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from multiprocessing import Process
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator, ValidationError
from datetime import date, datetime
import asyncpg
import logging

from db import create_pool, get_finished_scrapes_in_range, insert_practice_data

#
# Setup
#

# Config
load_dotenv()

config = {}
config['endpoint'] = os.getenv('ENDPOINT')
config['db_user'] = os.getenv('DB_USER')
config['db_password'] = os.getenv('DB_PASSWORD')
config['db_database'] = os.getenv('DB_NAME')
config['db_host'] = os.getenv('DB_HOST')
config['db_port'] = os.getenv('DB_PORT')
config['num_procs'] = os.getenv('WORKERS')
config['chunk_size'] = os.getenv('CHUNK_SIZE')
config['start_id'] = os.getenv('START_ID')
config['end_id'] = os.getenv('END_ID')

missing_fields = [field for field, value in config.items() if value is None]
if len(missing_fields):
    print(f'Missing config values {missing_fields}')
    sys.exit(1)

config['num_procs'] = int(config['num_procs'])
config['chunk_size'] = int(config['chunk_size'])
config['start_id'] = int(config['start_id'])
config['end_id'] = int(config['end_id'])

# Logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - pid_%(process)d - %(message)s', 
                    handlers=[logging.FileHandler(os.path.join(log_dir, 'scraper.log'))])
logger = logging.getLogger()


class PracticeData(BaseModel):
    id: int
    name: str
    registered_date: date
    status: str
    dispensing_license: bool

    @field_validator('registered_date', mode='before')
    @classmethod
    def parse_date(cls, v:str) -> date:
        return datetime.strptime(v, '%d-%m-%Y').date()


def extract_practice_data_from_html(html:str) -> dict | None:
    """
    Returns parsed dict of data extracted from html table, or None if missing table
    """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table')

    field_name_map = {
        'Practice Number': 'id',
        'Name': 'name',
        'Date Registered': 'registered_date',
        'Status': 'status',
        'Dispensing License': 'dispensing_license'
    }

    # if we find a table, it's a hit and there's data
    if table:
        data = {
            field_name_map[th.text.strip()] : td.text.strip() 
            for th, td 
            in zip(table.find_all('th'), table.find_all('td'))}
        parsed_data = PracticeData(**data)
        return parsed_data.model_dump()
    else:
        return None


async def get_practice_html(session:aiohttp.client.ClientSession, id:int, endpoint:str) -> str | None:
    """
    Returns html page string from post request to endpoint, or None on error 
    """
    payload = payload = {
        '__RequestVerificationToken': 'v3WB8xEFAsNG5LIa9AnNMpXhmTg0-mPJkXSs-a-o1YW0Ln2o0VqevK_2W1wll196o3i2OKISW5tbg4RKnLrJb9rLTlBNtU6LmWieXVS3H381',
        'SearchValue': id
    }

    try:
        async with session.post(endpoint, data=payload) as response:
            return await response.text()
    except aiohttp.ClientError as e:
        logger.error(f'ClientError for id {id}')
    return None


async def scrape_practice(id:int, session: aiohttp.client.ClientSession, pool: asyncpg.pool.Pool):
    """
    Get's html for a practice number, tries to extract data and save it to the db
    """
    html = await get_practice_html(session, id, config['endpoint'])
    if html is None: return

    try:
        data = extract_practice_data_from_html(html)
        await insert_practice_data(data, pool)
    except ValidationError as e:
        logger.error(f'ValidationError for id {id}')
        for error in e.errors():
            logger.error(repr(error))
    

async def scrape_in_range(worker_id:int, start_id:int, end_id:int, chunk_size:int):
    pool = await create_pool(config['db_user'], config['db_password'], config['db_database'], config['db_host'], config['db_port'])

    finished_scrapes = await get_finished_scrapes_in_range(pool, start_id, end_id)
    
    async with aiohttp.ClientSession() as session:
        for chunk_start_id in range(start_id, end_id, chunk_size):
            chunk_end_id = min(chunk_start_id + chunk_size, end_id)
            tasks = [scrape_practice(id, session, pool) for id in range(chunk_start_id, chunk_end_id) if id not in finished_scrapes]
            await asyncio.gather(*tasks)

            logger.info(f'Worker {worker_id} chunk {chunk_start_id}-{chunk_end_id} complete.')
    await pool.close()

#
# Worker process
#
def run_worker_process(worker_id:int, start_id:int, end_id:int, chunk_size:int):
    logger.info(f'Worker {worker_id} starting...')
    loop = asyncio.get_event_loop()
    task = scrape_in_range(worker_id, start_id, end_id, chunk_size)
    loop.run_until_complete(task)
    logger.info(f'Worker {worker_id} finished.')

#
# Main process
#
def main(start_id:int, end_id:int, num_procs:int, chunk_size:int):
    proc_list = []
    total_ids = (end_id + 1 - start_id) # +1 to include last number

    for i in range(num_procs):
        proc_start_id = start_id + i * total_ids // num_procs
        proc_end_id = start_id + (i + 1) * total_ids // num_procs
        proc = Process(target=run_worker_process, args=(i, proc_start_id, proc_end_id, chunk_size))
        proc_list.append(proc)
        proc.start()
    
    for proc in proc_list:
        proc.join()

    
    
if __name__ == '__main__':
    print('*'*20, f"Scrape started (Workers: {config['num_procs']}, Chunk size: {config['chunk_size']})...", '*'*20, sep='\n')
    main(config['start_id'], config['end_id'], config['num_procs'], config['chunk_size'])
    print('*'*20, 'Scrape complete.', '*'*20, sep='\n')

