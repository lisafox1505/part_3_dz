import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5005))
try:
    while True:
        accept_message, addr = sock.recvfrom(1024)
        two_numbers = accept_message.decode("utf-8")
        print(f"Прийнято {two_numbers}")

        try:
            two_number_split = two_numbers.split(",")
            result = str(sum(list(map(int, two_number_split))))
            print(f"Результат для відправки {result}")

            sock.sendto(result.encode("utf-8"), addr)
            print("Відправлено")
        except ValueError as e:
            send_message = f"Error: {e}"
            sock.sendto(send_message.encode("utf-8"), addr)

finally:
    sock.close()

