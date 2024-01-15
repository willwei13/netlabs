class Table:
    def __init__(self):
        self.ip = []
        self.mask = []
        self.line = []


def add_table(new_ip,new_mask,new_line):
    table.ip.append(new_ip)
    table.mask.append(new_mask)
    table.line.append(new_line)


def maketable():
    table.ip.append("255.0.0.0")
    table.ip.append("255.255.0.0")
    table.ip.append("255.255.255.0")
    table.mask.append(8)
    table.mask.append(16)
    table.mask.append(24)
    table.line.append(1)
    table.line.append(2)
    table.line.append(3)



def trans(ip):
    binary_ip = ''.join([bin(int(x) + 256)[3:] for x in ip.split('.')])
    return binary_ip


def ip_router(myip):
    lines = []
    binary_myip = trans(myip)
    for i in range(0,len(table.mask)):
        table_ip = table.ip[i]
        table_mask = table.mask[i]
        table_line = table.line[i]
        binary_tableip = trans(table_ip)
        count = 0

        for j in range(0,table_mask):
            if binary_tableip[j] == binary_myip[j]:
                 count += 1
        if count == table_mask:
            lines.append(table_line)
    return lines


if __name__ == '__main__':
    table = Table()
    maketable()
    add_table("172.0.0.0",8,4)

    myip = input("请输入IP地址：")
    my_lines = ip_router(myip)

    for i in range(0,len(my_lines)):
        my_line = my_lines[i]
        new_ip = trans(table.ip[my_line-1])
        new_mask = table.mask[my_line-1]
        print(f"cidr地址是{new_ip}/{new_mask}")

