from socket import *

class Client:
    def __init__(self,name):
        self.name = name
        self.port_session = -1

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 1025
    name = input("请输入用户名:\n")
    client = Client(name)
    s = socket(AF_INET, SOCK_DGRAM)
    message = client.name+','+str(client.port_session) +',' + "start"
    s.sendto(message.encode('utf-8'),(host,port))
    receive_message, _ = s.recvfrom(2048)
    receive_message = receive_message.decode()[19:]
    client.port_session = int(receive_message)
    print(f"{client.port_session}")
    while True:
        mymessage = input().split(',')
        option = mymessage[0]
        mess = mymessage[1]
        if option == "join":
            if mess != client.port_session:
                sock1 = socket(AF_INET, SOCK_DGRAM)
                message = client.name + ',' + str(mess) + ',' + "join"
                sock1.sendto(message.encode('utf-8'), (host, port))
                receive_message, _ = sock1.recvfrom(2048)
                receive_message = receive_message.decode()
                id = int(receive_message)
                client.port_session = id
                print(f"加入聊天室 {client.port_session}")


        if option == "leave":
            sock2 = socket(AF_INET, SOCK_DGRAM)
            message = client.name + ',' + str(client.port_session) + ',' + "leave"
            sock2.sendto(message.encode('utf-8'), (host, port))
            client.port_session = -1

        if option == "send":
            sock3 = socket(AF_INET, SOCK_STREAM)
            sock3.connect((host, client.port_session))
            message = client.name + ',' + str(client.port_session) + ',' + "send," + mess
            sock3.send(message.encode('utf-8'))
            data = sock3.recv(2048)
            print(data)
            sock3.close()
