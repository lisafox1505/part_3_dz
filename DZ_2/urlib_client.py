import json
from urllib import request, error

url = "https://jsonplaceholder.typicode.com"

try:
    with request.urlopen("{}/posts/2".format(url)) as response:
        headers = response.headers
        print(headers)

        read_response = response.read()
        decoder_response = read_response.decode("utf-8")
        response_json = json.loads(decoder_response)

        print("Заголовок: {}".format(response_json["title"]))
        print("ID користувача: {}".format(response_json["userId"]))

except error.HTTPError as e:
    e = e.read().decode("utf-8")
    print(e)

posts_test = {
    "title": "Вчимо Python",
    "body": "Практика urllib",
    "userId": 1
}

json_posts_test = json.dumps(posts_test)

send_message = request.Request("{}/posts".format(url), data=json_posts_test.encode("utf-8"), method="POST")
send_message.add_header("Content-Type", "application/json; charset=utf-8")

try:
    with request.urlopen(send_message) as response:
        read_result = response.read().decode("utf-8")

        print("-" * 30)
        print("Статус сервера: {}".format(response.status))
        print("Відповідь сервера: {}".format(read_result))

except error.HTTPError as e:
    e = e.read().decode("utf-8")
    print(e)




















# 1. Кодируем словарь в JSON-строку и переводим в байты
# data_json = json.dumps(new_post).encode('utf-8')
#
# # 2. Создаем объект запроса и добавляем заголовки
# req = urllib.request.Request(url, data=data_json, method='POST')
# req.add_header('Content-Type', 'application/json; charset=utf-8')
#
# try:
#     with urllib.request.urlopen(req) as response:
#         # Читаем ответ сервера (он должен вернуть созданный объект с ID)
#         res_data = response.read().decode('utf-8')
#         print("\n--- POST Результат ---")
#         print(f"Статус сервера: {response.status}")
#         print(f"Ответ сервера: {res_data}")
#
# except urllib.error.HTTPError as e:
#     print(f"Ошибка сервера: {e.code}")