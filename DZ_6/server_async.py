import asyncio


async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Підключився клієнт: {addr}")

    while True:
        data = await reader.read(1024)

        if not data:
            print("Клієнт закрив з'єднання")
            break

        message = data.decode()
        print(f"Отримано: {message}")
        response = f"Повідомлення: '{message}' отримано".encode()

        writer.write(response)
        await writer.drain()

    print("Закриваємо зв'язок...")
    writer.close()
    await writer.wait_closed()

async def main():

    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Сервер запущено на {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())