from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from well.frontend.chatbot import ChatBot
import uvicorn

app = FastAPI()
bot = ChatBot()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {"Server": "Running"}

@app.post("/send")
def get_response(input_text: str):
    input_text = str(input_text)
    response = bot.predict(input_text)
    latest_reply = response[-1][1] if response else None
    return {"response": latest_reply}


if __name__ == "__main__":
    uvicorn.run("well.api.main:app", host="127.0.0.1", port=8080)
