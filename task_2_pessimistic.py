import hazelcast
import threading
import time


def pessimistic_update():
    for i in range(1000):
        hz_map.lock(key)
        try:
            val = hz_map.get(key)
            time.sleep(0.001)
            val += 1
            hz_map.put(key, val)
        finally:
            hz_map.unlock(key)


if __name__ == "__main__":
    hz = hazelcast.HazelcastClient()
    hz_map = hz.get_map("my-distributed-map").blocking()

    key = 0
    init_val = 0
    hz_map.put(key, init_val)

    threads = []
    for i in range(3):
        thread = threading.Thread(target=pessimistic_update, name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Result = {hz_map.get(key)}")

    hz.shutdown()
