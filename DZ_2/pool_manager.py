import requests

from requests.adapters import HTTPAdapter

HOST = "http://127.0.0.1:8000/"

adapter = HTTPAdapter(pool_maxsize=10,
                      pool_connections=10)
session = requests.Session()
session.mount("http://", adapter=adapter)
for _ in range(100):
    print(session.get("http://127.0.0.1:8000/").text)
