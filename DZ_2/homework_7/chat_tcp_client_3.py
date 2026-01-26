import time

import requests


HOST_SERVER = "http://127.0.0.1:8000"
messages_list_for_send = {"127.0.0.1:7777": "Hello, this is Client 3", "127.0.0.1:8888": "Hello hello"}
print("Client 3: 127.0.0.1:9999\n")

for host, mess in messages_list_for_send.items():
    try:
        send_message = requests.post(HOST_SERVER, json={"message": mess, "HOST": host, "sender": "Client 3"})
        send_message.raise_for_status()
        print(f"Message: ({mess}) send to {host}\n")

    except requests.exceptions.RequestException as e:
        print("Error", e)

while True:
    try:
        accept_message = requests.post(HOST_SERVER, json={"check_mail": "", "HOST": "127.0.0.1:9999"})
        accept_message.raise_for_status()

        accept_message_json = accept_message.json()
        message_data = accept_message_json["message"]

        if message_data:
            print(f"Number of messages: {len(message_data)}")
            for i in message_data:
                text = i[0]
                sender = i[1]
                print(f"Sender: {sender} | Message: {text}")
        else:
            print("No message")

    except requests.exceptions.RequestException as e:
        print("Error", e)

    time.sleep(2)