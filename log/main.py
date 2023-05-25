import hazelcast
from consul import Consul
from fastapi import  FastAPI
from models.message import Message


consul = Consul()
app = FastAPI()

hz = hazelcast.HazelcastClient()
db = hz.get_map(consul.kv.get('map-name')[1]['Value'].decode('utf-8')).blocking()
# db = hz.get_map("my-distributed-map").blocking()

@app.get("/")
async def get_messages() -> str:
    return ";".join(db.values())


@app.post("/")
async def add_message(message: Message) -> str:
    print("Received message:", message.msg)
    db.put(message.uuid, message.msg)
    return message.msg


if __name__ == "__main__":
    import json
    import uvicorn
    import sys

    f = open("services_config.json", mode="r", encoding="UTF-8")
    cfg = json.load(f)

    port = int(sys.argv[1])
    if port not in cfg["ports"]["logging"]:
        print('\nInvalid port. Valid ports: ', cfg["ports"]["logging"])
        exit(1)

    consul.agent.service.register("Logging", "Logging" + str(port), cfg["host"], port)
    try:
        uvicorn.run(app="log.main:app",
                host=cfg["host"],
                port=port,
                reload=cfg["reload"],
                log_level=cfg["log_level"])
    except Exception as e:
        print(e)
