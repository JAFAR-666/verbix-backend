from fastapi import APIRouter
from ai_engine.gd_engine import generate_gd_topic, get_gd_response
from ai_engine.gd_evaluator import evaluate_gd

router = APIRouter()

@router.get("/gd/start")
def start_gd():
    topic = generate_gd_topic()
    return {"topic": topic}


@router.post("/gd/respond")
def gd_respond(user_input: str, topic: str, turn: int):

    responses = []

    # 3 AI participants
    for i in range(3):
        ai_reply = get_gd_response(user_input, topic, turn + i)
        responses.append(ai_reply)

    return {"responses": responses}

@router.post("/gd/evaluate")
def gd_evaluate(chat_history: list):
    result = evaluate_gd(chat_history)
    return result