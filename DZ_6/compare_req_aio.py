import asyncio
import sqlite3
from pprint import pprint

import aiohttp
import requests

urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://rickandmortyapi.com/api/character",
    "https://pokeapi.co/api/v2/pokemon",
    "https://catfact.ninja/fact"
]


def create_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    create_table = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL
    );
    """
    cursor.execute(create_table)
    conn.commit()
    conn.close()


def save_to_db(data, db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (action) VALUES (?)", data)
    conn.commit()
    conn.close()


def enquiry_with_request(url_name, db_name, table_name):
    action_first = f"Початок запиту до сайту {url_name}"
    save_to_db([action_first], db_name, table_name)
    try:
        response = requests.get(url_name)
        data_json = response.json()
        action_second = f"Відповідь від сайту {url_name} отримана (200)"
        pprint(f"{str(data_json)[:200]}...")

    except Exception as e:
        print(f"Помилка: {e}")
        action_second = f"Відповідь від сайту {url_name} відсутня (500)"

    save_to_db([action_second], db_name, table_name)


async def fetch_json_with_aiohttp(session, url_name, db_name, table_name):
    action_first = f"Початок запиту до сайту {url_name}"
    save_to_db([action_first], db_name, table_name)
    try:
        async with session.get(url_name) as response:
            result = await response.json()
            action_second = f"Відповідь від сайту {url_name} отримана (200)"
            save_to_db([action_second], db_name, table_name)
            return result

    except Exception as e:
        print(f"Помилка: {e}")
        action_second = f"Відповідь від сайту {url_name} відсутня (500)"
        save_to_db([action_second], db_name, table_name)
        return None


async def enquiry_with_aiohttp(db_name, table_name):
    async with aiohttp.ClientSession() as session:
        urls_list = [fetch_json_with_aiohttp(session, url, db_name, table_name) for url in urls]
        result = await asyncio.gather(*urls_list)
        pprint(f"{str(result)[:200]}...")


if __name__ == "__main__":
    create_db("db_logs.sqlite", "requests_logs")
    create_db("db_logs.sqlite", "aiohttp_logs")

    for url in urls:
        enquiry_with_request(url, "db_logs.sqlite", "requests_logs")

    asyncio.run(enquiry_with_aiohttp("db_logs.sqlite", "aiohttp_logs"))

