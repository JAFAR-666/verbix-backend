import random
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except:
        return ""

# -----------------------------
# ADVANCED GD ENGINE
# -----------------------------
def get_gd_responses(user_input, topic, history):

    history_text = "\n".join([f"{r}: {m}" for r, m in history[-10:]])

    leader = call_ai(f"""
You are a confident GD leader.

Topic: {topic}

Discussion:
{history_text}

User: {user_input}

Speak strongly and add a new point.
Keep it 1-2 lines.
""") or "I strongly believe this topic is important."

    opponent = call_ai(f"""
You are an opponent.

Leader said: {leader}

Interrupt and disagree strongly.
""") or "I disagree with that point."

    neutral = call_ai(f"""
You are neutral.

Leader: {leader}
Opponent: {opponent}

Balance both sides.
""") or "Both views are valid."

    question = call_ai(f"""
Ask a follow-up question to the user.

Topic: {topic}
""") or "Can you justify your opinion?"

    return [leader, opponent, neutral, question]


# -----------------------------
# AI EVALUATION
# -----------------------------
def evaluate_gd(history):
    text = "\n".join([f"{r}: {m}" for r, m in history])

    result = call_ai(f"""
Evaluate this group discussion:

{text}

Give:
- Confidence score /10
- Relevance score /10
- Communication score /10

Also give short feedback.
""")

    return result