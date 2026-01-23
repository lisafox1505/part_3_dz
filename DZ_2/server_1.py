import json
import socketserver

class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data, socket = self.request
        try:
            data_json = json.loads(data.decode("utf-8"))
            print(f"\nAdress: {self.client_address[0]}")
            print(f"id: {data_json.get('id')}")
            print(f"Message: {data_json.get('message')}")
        except:
            print(f"Отримані сирі дані: {data}")

if __name__ == '__main__':
    print("START")
    with socketserver.UDPServer(("127.0.0.1", 5006), EchoUDPHandler) as server:
        server.serve_forever()