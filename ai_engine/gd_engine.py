import random
import requests

OLLAMA_URL = "https://abc123.ngrok-free.dev/api/generate"

# -----------------------------
# TOPIC
# -----------------------------
def generate_gd_topic():
    return random.choice([
        "Is AI replacing human jobs?",
        "Online learning vs offline learning",
        "Impact of social media on youth"
    ])

# -----------------------------
# AI CALL
# -----------------------------
def call_ai(prompt):
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return res.json().get("response", "").strip()
    except:
        return ""

# -----------------------------
# ADVANCED GD ENGINE
# -----------------------------
def get_gd_responses(user_input, topic, history):
    history_text = ""
    for role, msg in history[-10:]:
        history_text += f"{role}: {msg}\n"

    # LEADER
    leader = call_ai(f"""
You are a strong GD Leader.

Topic: {topic}

Discussion:
{history_text}

User: {user_input}

- Take strong position
- Add new idea
- Be confident
- 1-2 lines
""") or "I strongly believe this topic needs serious attention."

    # OPPONENT (interrupt + disagree)
    opponent = call_ai(f"""
You are an Opponent.

Leader said: {leader}

- Interrupt slightly
- Disagree strongly
- Challenge logic
- 1-2 lines
""") or "I disagree — that argument is not fully valid."

    # NEUTRAL
    neutral = call_ai(f"""
You are Neutral.

Leader: {leader}
Opponent: {opponent}

- Refer both
- Balance discussion
- Add insight
- 1-2 lines
""") or "Both perspectives are valid."

    # FOLLOW-UP QUESTION
    question = call_ai(f"""
You are a GD Moderator.

Topic: {topic}

Ask user a challenging follow-up question.

- Short
- Thought-provoking
""") or "Can you justify your point with an example?"

    return [leader, opponent, neutral, question]