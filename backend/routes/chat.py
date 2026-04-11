from fastapi import APIRouter
from pydantic import BaseModel
from ai_engine.chat_engine import get_ai_response
from ai_engine.evaluator import evaluate_response

router = APIRouter()

class ChatRequest(BaseModel):
    user_input: str

@router.post("/chat")
def chat(req: ChatRequest):
    ai_response = get_ai_response(req.user_input)
    feedback = evaluate_response(req.user_input)

    return {
        "response": ai_response,
        "feedback": feedback
    }