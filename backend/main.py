from fastapi import FastAPI
from .routes import chat
from .routes import gd

app = FastAPI()

app.include_router(gd.router)
app.include_router(chat.router)