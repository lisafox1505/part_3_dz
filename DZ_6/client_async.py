import asyncio


async def tcp_client(message):
    print(f"Телефонуємо на сервер...")
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f"Відправляємо: {message}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(1024)
    print(f"Відповідь від сервера: {data.decode()}")


    print("Вішаємо трубку.")
    writer.close()
    await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(tcp_client("Привіт від клієнта"))
