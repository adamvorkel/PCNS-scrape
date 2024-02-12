# pip install aiohttp[speedups]

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import threading
from multiprocessing import Process

from timeit import timeit 
import requests

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

#
# Sync
#
def scrape_practice_details_sync(id):
    # url = 'https://www.pcns.co.za/Search/Verify'
    url = 'http://localhost:3000/hit'
    payload = payload = {
        '__RequestVerificationToken': 'v3WB8xEFAsNG5LIa9AnNMpXhmTg0-mPJkXSs-a-o1YW0Ln2o0VqevK_2W1wll196o3i2OKISW5tbg4RKnLrJb9rLTlBNtU6LmWieXVS3H381',
        'SearchValue': id
    }
    r = requests.post(url, data=payload)
    data = extract_practice_data(r.text)
    return data

    
def scrape_practice_details_in_range_sync(start, end):
    for id in range(start, end):
        print(f'Start scrape id: {id}')
        scrape_practice_details_sync(id)
        print(f'End scrape id: {id}')

#
# -- Single-threaded
#

def run_sync_scrape(count):
    scrape_practice_details_in_range_sync(0, count)


#
# -- Multi-threaded
#
        
def run_multi_sync_scrape(count, num_threads):
    thread_list = []
    
    for i in range(num_threads):
        start_id = i * count // num_threads
        end_id = (i + 1) * count // num_threads
        thread = threading.Thread(target=scrape_practice_details_in_range_sync, args=(start_id, end_id))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

#
# Async 
#

async def scrape_practice_details_async(session, id):
    # url = 'https://www.pcns.co.za/Search/Verify'
    url = 'http://localhost:3000/hit'
    payload = payload = {
        '__RequestVerificationToken': 'v3WB8xEFAsNG5LIa9AnNMpXhmTg0-mPJkXSs-a-o1YW0Ln2o0VqevK_2W1wll196o3i2OKISW5tbg4RKnLrJb9rLTlBNtU6LmWieXVS3H381',
        'SearchValue': id
    }
    async with session.post(url, data=payload) as response:
        html = await response.text()
        data = extract_practice_data(html)
        return data

async def scrape_practice_details_in_range_async(start, end):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_practice_details_async(session, id) for id in range(start, end)]
        results = await asyncio.gather(*tasks)

#
# -- Single-threaded
#

def run_async_scrape(count):
    loop = asyncio.get_event_loop()
    task = scrape_practice_details_in_range_async(0, count)
    loop.run_until_complete(task)

#
# -- Multi-process
#

def run_async_scrape_process(start, end):
    loop = asyncio.get_event_loop()
    task = scrape_practice_details_in_range_async(start, end)
    loop.run_until_complete(task)

def run_multi_async_scrape(count, num_procs):
    process_list = []
    
    for i in range(num_procs):
        start_id = i * count // num_procs
        end_id = (i + 1) * count // num_procs
        process = Process(target=run_async_scrape_process, args=(start_id, end_id))
        process_list.append(process)
        process.start()
    
    for process in process_list:
        process.join()
    
    print('done')



if __name__ == '__main__':
    count = 20_000

    # print('Sync, single-thread...')
    # time = timeit(lambda: run_sync_scrape(count), number=1)
    # print(f'Sync, single-thread: {time}')

    # print('Sync, multi-thread 4...')
    # time = timeit(lambda: run_multi_sync_scrape(count, 4), number=1)
    # print(f'Sync, multi-thread 4: {time}')

    # print('Sync, multi-thread 8...')
    # time = timeit(lambda: run_multi_sync_scrape(count, 8), number=1)
    # print(f'Sync, multi-thread 8: {time}')

    # print('Sync, multi-thread 16...')
    # time = timeit(lambda: run_multi_sync_scrape(count, 16), number=1)
    # print(f'Sync, multi-thread 16: {time}')

    # print('Sync, multi-thread 32...')
    # time = timeit(lambda: run_multi_sync_scrape(count, 32), number=1)
    # print(f'Sync, multi-thread 32: {time}')

    # print('Async, single-process...')
    # time = timeit(lambda: run_async_scrape(count), number=1)
    # print(f'Async, single-process: {time}')

    # print('Async, multi-process 8...')
    # time = timeit(lambda: run_multi_async_scrape(count, 8), number=1)
    # print(f'Async, multi-process 8: {time}')

    for proc_count in [8, 16, 32, 40, 48]:
        time = timeit(lambda: run_multi_async_scrape(count, proc_count), number=1)
        print(f'Async, multi-process {proc_count}: {time}')
    