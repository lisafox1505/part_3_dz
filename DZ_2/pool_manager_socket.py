import socketserver

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: 13\r\n"
            "Connection: close\r\n"
            "\r\n"
            "Hello, world!\r\n"
        ).encode("utf-8")
        self.request.sendall(response)

HOST, PORT = "127.0.0.1", 8000
if __name__ == "__main__":
    with ThreadingTCPServer((HOST, PORT),
                                MyTCPHandler) as server:
        server.serve_forever()