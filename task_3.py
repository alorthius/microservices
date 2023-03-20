import hazelcast
import threading


def consumer():
    while True:
        item = hz_queue.take()
        print(f"Read: {item}")
        if item == -1:
            hz_queue.put(-1)
            break


def producer():
    for i in range(1000):
        hz_queue.put(i)
        print(f"Written: {i}")
        if i == 999:
            hz_queue.put(-1)
            print(f"Written: -1")


if __name__ == "__main__":
    hz = hazelcast.HazelcastClient()
    hz_queue = hz.get_queue("queue").blocking()

    producer = threading.Thread(target=producer, name="Producer")
    producer.start()

    # consumer_1 = threading.Thread(target=consumer, name="Consumer-1")
    # consumer_1.start()
    # consumer_2 = threading.Thread(target=consumer, name="Consumer-2")
    # consumer_2.start()

    producer.join()
    # consumer_1.join()
    # consumer_2.join()

    hz.shutdown()
