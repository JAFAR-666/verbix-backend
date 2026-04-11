import random
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"


def generate_gd_topic():
    topics = [
        "Is AI replacing human jobs?",
        "Impact of social media on youth",
        "Online learning vs offline learning",
        "Should college education be free?",
        "Is technology making people lazy?"
    ]
    return random.choice(topics)


def get_gd_response(user_input, topic, turn):
    try:
        # 🎭 Different personalities
        personalities = [
            "You are a confident speaker who strongly presents opinions.",
            "You are a critical thinker who questions others.",
            "You are a balanced participant who gives neutral views."
        ]

        personality = personalities[turn % len(personalities)]

        prompt = f"""
        {personality}

        Topic: {topic}

        User said: {user_input}

        Respond like a participant in a group discussion.
        Keep it short, natural, and relevant.
        """

        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return fallback_gd_response(user_input, topic)

    except Exception:
        return fallback_gd_response(user_input, topic)


# 🔁 Fallback GD logic (if Ollama fails)
def fallback_gd_response(user_input, topic):
    topic = topic.lower()

    if "ai" in topic:
        return random.choice([
            "AI is changing industries rapidly.",
            "It creates jobs but also replaces some roles.",
            "Human creativity will always be important."
        ])

    elif "social media" in topic:
        return random.choice([
            "Social media has both benefits and drawbacks.",
            "It connects people but can be addictive.",
            "It impacts mental health significantly."
        ])

    else:
        return random.choice([
            "That's an interesting point.",
            "I see your perspective.",
            "Can you explain further?"
        ])