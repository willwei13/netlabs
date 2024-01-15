import random
import time
import matplotlib.pyplot as plt

class Packet:
    def __init__(self, data):
        self.data = data
        self.hops = 0
        self.error = random.random() < 1
        self.acknowledged = False

class Router:
    def __init__(self, name, buffer_size, hop_interval, discard_interval):
        self.name = name
        self.buffer_size = buffer_size
        self.buffer = []
        self.successful_transmissions = []
        self.hop_interval = hop_interval
        self.discard_interval = discard_interval
        self.last_hop_time = time.time()
        self.last_transmission_time = time.time()
        self.last_discard_time = time.time()

    def receive_packet(self, packet):
        current_time = time.time()
        if len(self.buffer) > 0 and current_time - self.last_discard_time >= self.discard_interval:
            self.buffer.pop(0)
            self.last_discard_time = current_time
        if len(self.buffer) < self.buffer_size:
            self.buffer.append(packet)
        else:
            print(f"{self.name}:缓冲区满了")

    def process_packets(self):
        current_time = time.time()
        for packet in self.buffer:
            packet.hops += 1
            if current_time - self.last_hop_time >= self.hop_interval:
                if not packet.error:
                    self.successful_transmissions.append(packet.data)
                    packet.acknowledged = True
                    self.last_transmission_time = current_time
                self.buffer.remove(packet)
                self.last_hop_time = current_time
        if current_time - self.last_transmission_time >= 2 * self.hop_interval:
            for packet in self.buffer:
                if not packet.acknowledged:
                    print(f"{self.name}:  {packet.data}超时重传")
                    packet.acknowledged = True
                    self.last_transmission_time = current_time


def plot_throughput(error_rates, timeout_intervals):
    throughputs = []
    for error_rate in error_rates:
        row_throughputs = []
        for interval in timeout_intervals:
            router1 = Router("Router1", 2, interval, 1e-4)
            router2 = Router("Router2", 2, interval, 1e-4)

            for char in packets:
                packet = Packet(char)
                router1.receive_packet(packet)
                router2.receive_packet(router1.buffer.pop(0))
                router1.process_packets()
                router2.process_packets()
            row_throughputs.append(len(router2.successful_transmissions))
        throughputs.append(row_throughputs)
    for i, error_rate in enumerate(error_rates):
        plt.plot(timeout_intervals, throughputs[i], label=f"rate: {error_rate}")

    plt.xlabel("time")
    plt.ylabel("capacity")
    plt.legend()
    plt.show()


def simulatenetwork(packets):
    router1 = Router("Router1", 2, 1e-4, 1e-4)
    router2 = Router("Router2", 2, 1e-4, 1e-4)

    for char in packets:
        packet = Packet(char)
        router1.receive_packet(packet)
        router2.receive_packet(router1.buffer.pop(0))

        router1.process_packets()
        router2.process_packets()

    print("\nRouter1:")
    print([packet.data for packet in router1.buffer])
    print("\nRouter2:")
    print([packet.data for packet in router2.buffer])


if __name__ == "__main__":
    packets = input("输入要传输的数据包: ")
    simulatenetwork(packets)
    error_rates = [0.2, 0.5, 0.75]
    timeout_intervals = [1e-4, 1e-3 , 1e-2]
    #plot_throughput(error_rates, timeout_intervals)