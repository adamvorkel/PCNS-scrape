import asyncpg
import logging

logger = logging.getLogger()

async def create_pool(user:str, password:str, database:str, host:str, port:str):
    return await asyncpg.create_pool(
        user=user,
        password=password,
        database=database,
        host=host,
        port=port,
        # min_size=10,
        # max_size=48
    )

async def get_finished_scrapes_in_range(pool:asyncpg.pool.Pool, start_id:int, end_id:int):
    """
    Get ordered list of completed scrape ids in range between start_id and end_id from scrape_results table
    """
    async with pool.acquire() as connection:
        try:

            async with connection.transaction():
                result = await connection.fetch('SELECT id FROM scrape_results WHERE id BETWEEN $1 AND $2 ORDER BY id', start_id, end_id)
                return [record['id'] for record in result]
        except asyncpg.PostgresError as e:
            logger.error(f'PostgresError: {e}')   


async def insert_practice_data(data:dict, pool:asyncpg.pool.Pool):
    """
    Save practice data to practice table if present
    Save scrape outcome to scrape_results table
    """
    async with pool.acquire() as connection:
        try:
            if data is not None:
                async with connection.transaction():
                    await connection.execute('INSERT INTO scrape_results (id, success) VALUES ($1, $2)', data['id'], True)
                    await connection.execute('INSERT INTO practices (id, name, registered_date, status, dispensing_license) VALUES ($1, $2, $3, $4, $5)', 
                                            data['id'], data['name'], data['registered_date'], data['status'], data['dispensing_license'])
            else:
                await connection.execute('INSERT INTO scrape_results (id, success) VALUES ($1, $2)', data['id'], False)
        except asyncpg.PostgresError as e:
            logger.error(f'PostgresError: {e}')
        