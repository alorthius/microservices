import json
import uvicorn
import httpx
import asyncio
from fastapi import FastAPI
from models.message import RawMessage

def get_url(host: str, port: str):
    return f"http://{host}:{port}"

f = open("services_config.json", mode="r", encoding="UTF-8")
cfg = json.load(f)

logging_url = get_url(cfg["host"], str(cfg["ports"]["logging"]))
messages_url = get_url(cfg["host"], str(cfg["ports"]["messages"]))


app = FastAPI()


async def send_GET_request(client, url) -> (str, int):
    response = await client.get(url)
    return response.json(), response.status_code


async def send_POST_request(client, url, message: RawMessage) -> (str, int):
    response = await client.post(url, json={"msg": message.msg})
    return response.json(), response.status_code


async def task_GET() -> str:
    async with httpx.AsyncClient() as client:
        # Schedule both concurrently
        res = await asyncio.gather(send_GET_request(client, logging_url),
                                   send_GET_request(client, messages_url))
        return f"Response from logging:  `{res[0][0]}` with status {res[0][1]}\nResponse from messages: `{res[1][0]}` with status {res[1][1]}\n"


async def task_POST(message: RawMessage):
    async with httpx.AsyncClient() as client:
        return await send_POST_request(client, logging_url, message)


@app.get('/')
async def process_GET():
    result = await task_GET()
    return result


@app.post("/")
async def process_POST(message: RawMessage):
    result = await task_POST(message)
    return result[0]


if __name__ == "__main__":
    uvicorn.run(app="facade.main:app",
                host=cfg["host"],
                port=cfg["ports"]["facade"],
                reload=cfg["reload"],
                log_level=cfg["log_level"])
