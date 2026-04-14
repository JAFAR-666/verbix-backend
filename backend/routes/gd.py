from fastapi import APIRouter
from ai_engine.gd_engine import generate_gd_topic, get_gd_responses, evaluate_gd

router = APIRouter()

@router.get("/gd/start")
def start():
    return {"topic": generate_gd_topic()}

@router.post("/gd/respond")
def respond(data: dict):
    responses = get_gd_responses(
        data["user_input"],
        data["topic"],
        data["history"]
    )

    return {
        "leader": responses[0],
        "opponent": responses[1],
        "neutral": responses[2],
        "question": responses[3]
    }

@router.post("/gd/evaluate")
def evaluate(data: dict):
    result = evaluate_gd(data["history"])
    return {"result": result}