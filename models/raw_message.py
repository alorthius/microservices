from pydantic import BaseModel, Field, ValidationError, validator


class RawMessage(BaseModel):
    msg: str

if __name__ == "__main__":
    print(RawMessage(msg="message 1"))
    print(RawMessage(msg="message 2"))
    print(RawMessage(msg="message 3"))
