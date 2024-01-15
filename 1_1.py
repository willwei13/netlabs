MAX_MESSAGE_SIZE = 80
MAX_HEADER_SIZE = 64


def application_layer(message,size):
    head = "application head"
    if len(head)<=MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        presentation_layer(newmassage,len(newmassage))
    else:
        print("application head is too long")


def presentation_layer(message,size):
    head = "presentation head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        session_layer(newmassage, len(newmassage))
    else:
        print("presentation head is too long")


def session_layer(message,size):
    head = "session head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        transport_layer(newmassage, len(newmassage))
    else:
        print("session head is too long")


def transport_layer(message,size):
    head = "transport head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        network_layer(newmassage, len(newmassage))
    else:
        print("transport head is too long")


def network_layer(message,size):
    head = "network head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        data_link_layer(newmassage, len(newmassage))
    else:
        print("network head is too long")


def data_link_layer(message,size):
    head = "data link head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
        physical_layer(newmassage, len(newmassage))
    else:
        print("data link head is too long")


def physical_layer(message,size):
    head = "physical head"
    if len(head) <= MAX_HEADER_SIZE:
        newmassage = head + " " + message + " "
        print(newmassage)
    else:
        print("physical link head is too long")

if __name__ == '__main__':
    message = input("请输入一条应用程序信息：")
    if len(message)<=MAX_MESSAGE_SIZE:
        application_layer(message,len(message))
    else:
        print("message is too long")
