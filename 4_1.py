import time
import threading


class myclass:

    def __init__(self, name, frame_count):
        self.name = name
        self.frame_count = frame_count
        self.attempts = 0

    def send_frame(self):
        backoff_time = self.binary_backoff()
        print(f"{self.name}: 等待 {backoff_time} ")
        time.sleep(backoff_time * slot_time)

        if not channel_busy():
            occupy_channel()
            print(f"{self.name}: 发送时间是{int(time.time() / slot_time)} ")
            time.sleep(frame_transmission_time)
            release_channel()
        else:
            print(f"{self.name}:出现冲突")
            self.attempts += 1


    def binary_backoff(self):
        return 2 ** min(self.attempts, 10)


def channel_busy():
    return channel_occupied


def occupy_channel():
    global channel_occupied
    channel_occupied = True


def release_channel():
    global channel_occupied
    channel_occupied = False


def station_behavior(station):
    for _ in range(station.frame_count):
        station.send_frame()


if __name__ == "__main__":
    slot_time = 5.12e-4
    frame_transmission_time = 1
    channel_occupied = False

    N = int(input("请输入站的数量："))
    n = int(input("请输入要传输的帧的数量： "))

    stations = []
    for i in range(N):
        station_name = f"Station {i + 1}"
        station = myclass(station_name, n)
        station_thread = threading.Thread(target=station_behavior, args=(station,))
        stations.append(station_thread)

    for station in stations:
        station.start()

    for station in stations:
        station.join()
