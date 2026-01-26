import json
import socketserver

mailboxes = {}

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class TcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(4096).decode("utf-8")

        if "\r\n\r\n" in data:
            json_part = data.split("\r\n\r\n")[1]
        else:
            return

        if not json_part:
            return

        data_dict = json.loads(json_part)
        sender = data_dict.get("sender", None)
        client_for_send = data_dict.get("HOST", None)

        if "message" in data_dict:
            message = data_dict.get("message", [])

            if client_for_send not in mailboxes:
                mailboxes[client_for_send] = []
            mailboxes[client_for_send].append((message, sender))
            response_body = json.dumps({"status": "saved"})

        elif "check_mail" in data_dict:
            client_for_send = data_dict.get("HOST")
            message_data = mailboxes.get(client_for_send, [])
            response_body = json.dumps({"message": message_data})
            mailboxes[client_for_send] = []


        else:
            response_body = json.dumps({"error": "Unknown command"})

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
            "\r\n"
            f"{response_body}"
        )

        self.request.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    print("START")
    with ThreadingTCPServer(("127.0.0.1", 8000), TcpHandler) as server:
        server.serve_forever()