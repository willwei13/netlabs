from socket import *
from threading import Thread
from random import randint
import socketserver
from server import Server


class coordinator:
    def __init__(self):
        self.clients = {}
        self.serves = {}


if __name__ == '__main__':
    host = "127.0.0.1"
    coordinator_host = "0.0.0.0"
    port = 1025
    coordinator = coordinator()
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((coordinator_host, port))
    while True:
        data, addr = sock.recvfrom(2048)
        print(f" 从 {addr} 收到信息 {data} ")
        receive = data.decode().split(',')
        name = receive[0]
        user_port = int(receive[1])
        optional = receive[2]
        print(f"从聊天室 {user_port} 中的用户 {name} 收到 {optional} .")

        if optional == 'start':
            id = randint(0, 65536)
            coordinator.clients.setdefault(id, []).append(name)
            server = socketserver.ThreadingTCPServer((host, id), Server)
            coordinator.serves[id] = server
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            response = "your session_id is " + str(id)
            sock.sendto(response.encode('utf8'), addr)
            print(f"用户 {name} 被分配到聊天室 {id}")
        elif optional == "leave":
            users = coordinator.clients.get(user_port)
            if users:
                users.remove(name)
                if len(users) == 0:
                    del coordinator.clients[user_port]
            print(f"用户 {name} 从聊天室 {user_port} 离开")

        elif optional == "join":
            id = int(receive[1])
            users = coordinator.clients.get(id)
            if users:
                coordinator.clients.setdefault(id, []).append(name)
                message = str(id)
                sock.sendto(message.encode('utf-8'), addr)
                print(f"用户 {name} 加入了聊天室 {id}.")
        else:
            continue

        print(f"可用的聊天室和加入的用户为:")
        for str1, str2 in coordinator.clients.items():
            print(f"{str1}:{str2}\t")
