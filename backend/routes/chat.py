from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

class ChatRequest(BaseModel):
    message: str
    history: list = []

@router.post("/chat")
def chat(req: ChatRequest):
    try:
        # 🧠 Build conversation memory
        history_text = ""
        for role, msg in req.history[-5:]:
            history_text += f"{role}: {msg}\n"

        prompt = f"""
You are Verbix, a friendly AI communication coach.

Guidelines:
- Speak naturally like a human
- Keep answers short (2-4 lines)
- Be engaging and conversational
- Avoid robotic explanations

Conversation:
{history_text}

User: {req.message}
Verbix:
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = response.json()
        return {"response": data.get("response", "Hmm, tell me more.")}

    except Exception as e:
        print("CHAT ERROR:", e)
        return {"response": "AI not responding"}