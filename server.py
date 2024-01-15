import socketserver

class Server(socketserver.BaseRequestHandler):
    chat_rooms = {}
    users_count = 0

    def setup(self):
        super().setup()

    def handle(self):
        super().handle()
        data = self.request.recv(2048)
        data = data.decode()
        data = data.split(',')
        username = data[0]
        session_id = int(data[1])
        action = data[2]

        if action == "send":
            messages = data[3:]
            print(f"收到消息{messages}")
            if session_id in self.chat_rooms:
                self.chat_rooms.setdefault(session_id, []).append([username, messages])
            else:
                self.users_count += 1
                self.chat_rooms.setdefault(session_id, []).append([username, messages])
            print(f"历史记录{self.chat_rooms}")
            self.request.send(str(self.chat_rooms[session_id]).encode('utf-8'))

    def finish(self):
        super().finish()
        self.request.close()
