import requests


url = "https://jsonplaceholder.typicode.com"

try:
    response = requests.get(f"{url}/posts/2")
    response.raise_for_status()

    response_json = response.json()

    print("Заголовок: {}".format(response_json["title"]))
    print("ID користувача: {}".format(response_json["userId"]))

except requests.exceptions.RequestException as e:
    print(e)

posts_test = {
    "title": "Вчимо Python",
    "body": "Практика urllib",
    "userId": 1
}
try:
    send_message = requests.post(f"{url}/posts", json=posts_test)
    send_message.raise_for_status()

    created_post = send_message.json()

    print("-" * 30)
    print(f"Статус сервера: {send_message.status_code}")
    print(f"Відповідь сервера: {created_post}")

except requests.exceptions.RequestException as e:
    print(e)
