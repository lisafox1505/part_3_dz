import json
import random
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
info = {"id": random.randint(100, 999), "message": "Пристрій підключен"}
message = json.dumps(info, ensure_ascii=False).encode("utf-8")
try:
    sock.sendto(message, ("127.0.0.1", 5006))
    print("Повіддомлення відправлено")
finally:
    sock.close()