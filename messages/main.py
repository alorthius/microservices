import logging

from fastapi import  FastAPI

app = FastAPI()


@app.get("/")
async def get_messages() -> str:
    logging.info("Messages processes GET request")
    return "Not implemented yet"


if __name__ == "__main__":
    import json
    import uvicorn

    f = open("services_config.json", mode="r", encoding="UTF-8")
    cfg = json.load(f)

    uvicorn.run(app="messages.main:app",
                host=cfg["host"],
                port=cfg["ports"]["messages"],
                reload=cfg["reload"],
                log_level=cfg["log_level"])
