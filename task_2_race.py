import hazelcast
import threading
import time


def raced_update():
    for i in range(1000):
        val = hz_map.get(key)
        time.sleep(0.001)
        val += 1
        hz_map.put(key, val)


if __name__ == "__main__":
    # Start the Hazelcast Client and connect to an already running Hazelcast Cluster on 127.0.0.1
    hz = hazelcast.HazelcastClient()
    # Get the Distributed Map from Cluster.
    hz_map = hz.get_map("my-distributed-map").blocking()

    key = 0
    init_val = 0
    hz_map.put(key, init_val)

    threads = []
    for i in range(3):
        thread = threading.Thread(target=raced_update, name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Result = {hz_map.get(key)}")

    # Shutdown this Hazelcast Client
    hz.shutdown()
