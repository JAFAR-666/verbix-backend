from fastapi import FastAPI
from backend.routes import chat
from backend.routes import gd

app = FastAPI()

app.include_router(gd.router)
app.include_router(chat.router)