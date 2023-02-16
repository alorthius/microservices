from uuid import uuid4
from pydantic import BaseModel, Field, ValidationError, validator


class Message(BaseModel):
    uuid: str = Field(default_factory=uuid4)
    msg: str


if __name__ == "__main__":
    print(Message(msg="message 1"))
    print(Message(msg="message 2"))
    print(Message(msg="message 3"))
