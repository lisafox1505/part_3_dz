import os
import time

os.system("start cmd /k python chat_tcp_server.py")

time.sleep(1)

os.system("start cmd /k python chat_tcp_client_1.py")

os.system("start cmd /k python chat_tcp_client_2.py")

os.system("start cmd /k python chat_tcp_client_3.py")
