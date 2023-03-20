import hazelcast
import threading
import time


def optimistic_update():
    for i in range(1000):
        while True:
            val = hz_map.get(key)
            time.sleep(0.001)
            new_val = val + 1
            if hz_map.replace_if_same(key, val, new_val):
                break


if __name__ == "__main__":
    hz = hazelcast.HazelcastClient()
    hz_map = hz.get_map("my-distributed-map").blocking()

    key = 0
    init_val = 0
    hz_map.put(key, init_val)

    threads = []
    for i in range(3):
        thread = threading.Thread(target=optimistic_update, name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Result = {hz_map.get(key)}")

    hz.shutdown()
