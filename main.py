from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple Deploy Demo API", version="1.0.0")


class Message(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "API is live and alam is talking to you hiii"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/echo")
def echo(message: Message):
    return {"you_sent": message.text, "length": len(message.text)}
