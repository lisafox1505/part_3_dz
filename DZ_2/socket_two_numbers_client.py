import socket

a = input("Перше число: ").strip()
b = input("Друге число: ").strip()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = f"{a}, {b}"
message = message.encode("utf-8")
sock.sendto(message,  ("127.0.0.1", 5005))

accept_message = sock.recv(1024)

print(f'Результат: {accept_message.decode("utf-8")}')

sock.close()