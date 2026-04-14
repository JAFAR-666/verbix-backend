from fastapi import APIRouter
from ai_engine.gd_engine import generate_gd_topic, get_gd_responses

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