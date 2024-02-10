# pip install aiohttp[speedups]

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import threading
from multiprocessing import Process

from timeit import timeit 
import requests
url = 'http://localhost:3000/hit'
def extract_practice_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table')

    # if we find a table, it's a hit and there's data
    if table:
        data = {
            th.text.strip() : td.text.strip() 
            for th, td 
            in zip(table.find_all('th'), table.find_all('td'))}
        return data
    else:
        return None





async def scrape_practice_details(session, id):
    # url = 'https://www.pcns.co.za/Search/Verify'
    
    payload = payload = {
        '__RequestVerificationToken': 'v3WB8xEFAsNG5LIa9AnNMpXhmTg0-mPJkXSs-a-o1YW0Ln2o0VqevK_2W1wll196o3i2OKISW5tbg4RKnLrJb9rLTlBNtU6LmWieXVS3H381',
        'SearchValue': id
    }
    async with session.post(url, data=payload) as response:
        html = await response.text()
        data = extract_practice_data(html)
        return data

async def scrape_practice_details_in_range(start, end):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_practice_details(session, id) for id in range(start, end)]
        results = await asyncio.gather(*tasks)

#
# -- Multi-process
#

def run_worker_process(start, end):
    loop = asyncio.get_event_loop()
    task = scrape_practice_details_in_range(start, end)
    loop.run_until_complete(task)

def main(count, num_procs):
    process_list = []
    
    for i in range(num_procs):
        start_id = i * count // num_procs
        end_id = (i + 1) * count // num_procs
        process = Process(target=run_worker_process, args=(start_id, end_id))
        process_list.append(process)
        process.start()
    
    for process in process_list:
        process.join()
    
    print('done')



if __name__ == '__main__':
    count = 20_000

    proc_count = 32
    time = timeit(lambda: main(count, proc_count), number=1)
    print(f'{proc_count} processes: {time}')
