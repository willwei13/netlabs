import copy

class Packet:
    def __init__(self, counter):
        self.counter = counter
        self.path = []

    def get_counter(self):
        return self.counter

    def get_path(self):
        return self.path

    def copy_packet(self):
        return copy.deepcopy(self)

class Node:
    def __init__(self, name):
        self.name = name
        self.adj_nodes = []

    def get_name(self):
        return self.name

    def get_adj_nodes(self):
        return self.adj_nodes

    def connect(self, nodes):
        for adj_node in nodes:
            self.adj_nodes.append(adj_node)

    def flood_version1(self, packet):
        packet.get_path().append(self.name)
        if packet.get_counter() == 0:
            print(f"传输路径是{packet.get_path()}")
        else:
            packet.counter -= 1
            for next_node in self.adj_nodes:
                next_node.flood_version1(packet.copy_packet())

    def flood_version2(self, packet, mynode):
        packet.get_path().append(self.name)
        if packet.get_counter() == 0:
            print(f"传输路径是 {packet.get_path()}")
        else:
            packet.counter -= 1
            for next_node in self.adj_nodes:
                if next_node != mynode:
                    next_node.flood_version2(packet.copy_packet(), mynode)

    def flood_version3(self, packet, best_line):
        packet.get_path().append(self.name)
        if packet.get_counter() == 0:
            print(f"传输路径是: {packet.get_path()}")
        else:
            packet.counter -= 1
            best_line.flood_version3(packet.copy_packet(), best_line)

    def choose_best_line(self, destination):
        return self.adj_nodes[0]

if __name__ == '__main__':
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')

    node_a.connect([node_b, node_c])
    node_b.connect([node_a, node_c, node_d])
    node_c.connect([node_a, node_b, node_d])
    node_d.connect([node_b, node_c])

    packets_to_send = [Packet(3), Packet(2), Packet(4)]

    for packet in packets_to_send:
        node_a.flood_version1(packet)

    for packet in packets_to_send:
        node_a.flood_version2(packet, node_a)

    for packet in packets_to_send:
        best_line = node_a.choose_best_line('D')
        node_a.flood_version3(packet, best_line)