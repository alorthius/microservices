import threading
import hazelcast
from fastapi import FastAPI
from contextlib import asynccontextmanager


hz = hazelcast.HazelcastClient()
queue = hz.get_queue("my-queue").blocking()
messages = []

def listen_queue():
    while True:
        if not queue.is_empty():
            message = queue.take()
            messages.append(message.msg)
            print(f"Received message: {message.msg}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=listen_queue)
    thread.start()
    yield
    thread.join()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get_messages() -> str:
    return ",".join(messages)


if __name__ == "__main__":
    import json
    import uvicorn
    import sys

    f = open("services_config.json", mode="r", encoding="UTF-8")
    cfg = json.load(f)
    port = int(sys.argv[1])
    if port not in cfg["ports"]["messages"]:
        print('\nInvalid port. Valid ports: ', cfg["ports"]["messages"])
        exit(1)

    uvicorn.run(app="messages.main:app",
                host=cfg["host"],
                port=port,
                reload=cfg["reload"],
                log_level=cfg["log_level"])

