from fastapi import  FastAPI
from models.message import Message


app = FastAPI()

db = dict()


@app.get("/")
async def get_messages() -> str:
    return ";".join(db.values())


@app.post("/")
async def add_message(message: Message) -> str:
    db[message.uuid] = message.msg
    return message.msg


if __name__ == "__main__":
    import json
    import uvicorn

    f = open("services_config.json", mode="r", encoding="UTF-8")
    cfg = json.load(f)

    uvicorn.run(app="log.main:app",
                host=cfg["host"],
                port=cfg["ports"]["logging"],
                reload=cfg["reload"],
                log_level=cfg["log_level"])
