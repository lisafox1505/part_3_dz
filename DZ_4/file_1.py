import datetime
import sqlite3
from pprint import pprint
import requests

conn = sqlite3.connect("my_bank.db")
cursor = conn.cursor()
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS exchange_rates (
#         id INTEGER PRIMARY KEY,
#         currency_name TEXT,
#         currency_value REAL,
#         current_date TEXT
#     )
# """)
# conn.commit()


url = "https://api.monobank.ua/bank/currency"
response = requests.get(url)
currency_data = response.json()
pprint(currency_data)

rate_gbp_uah = 0
rate_uah_usd = 0

for item in currency_data:
    curr_a = item["currencyCodeA"]
    curr_b = item["currencyCodeB"]
    currency_name = None
    rate = 0

    if curr_a == 840 and curr_b == 980:
        currency_name = "UAH"
        rate_uah_usd = item.get("rateSell") or item.get("rateCross")
        rate = rate_uah_usd

    elif curr_a == 978 and curr_b == 840:
        currency_name = "EUR"
        rate = item.get("rateSell") or item.get("rateCross")

    elif curr_a == 826 and curr_b == 980:
        rate_gbp_uah = item.get("rateSell") or item.get("rateCross")
        continue

    if currency_name is not None:
        now = datetime.datetime.now()
        cursor.execute("INSERT INTO exchange_rates (currency_name, currency_value, current_date) VALUES (?, ?, ?)",
                       (currency_name, rate, str(now)))
        conn.commit()

if rate_gbp_uah > 0 and rate_uah_usd > 0:
    rate = rate_gbp_uah / rate_uah_usd
    currency_name = "GBP"
    now = datetime.datetime.now()
    cursor.execute("INSERT INTO exchange_rates (currency_name, currency_value, current_date) VALUES (?, ?, ?)",
                   (currency_name, rate, str(now)))
    conn.commit()

conn.close()





