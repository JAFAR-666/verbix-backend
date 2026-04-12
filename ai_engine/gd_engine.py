import random
import requests

OLLAMA_URL = "https://flatly-agreeing-flyover.ngrok-free.dev/api/generate"
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
        roles = [
            ("Leader", "You lead the discussion with strong and clear opinions."),
            ("Opponent", "You politely disagree and give counter-arguments."),
            ("Neutral", "You provide a balanced and thoughtful perspective.")
        ]

        role_name, role_prompt = roles[turn % len(roles)]

        prompt = f"""
        {role_prompt}

        Topic: {topic}

        Previous speaker said: "{user_input}"

        Respond as a {role_name} in a group discussion.
        Keep response:
        - Relevant
        - Natural
        - Unique
        - 1-2 sentences only
        """

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("response", "").strip() or fallback_gd_response(user_input, topic)

        return fallback_gd_response(user_input, topic)

    except Exception:
        return fallback_gd_response(user_input, topic)


def fallback_gd_response(user_input, topic):
    topic = topic.lower()

    if "ai" in topic:
        return random.choice([
            "AI is transforming industries but also creating new opportunities.",
            "Human creativity still plays a major role alongside AI.",
            "Automation may replace repetitive jobs but not complex thinking."
        ])

    elif "social media" in topic:
        return random.choice([
            "Social media connects people but can also distract.",
            "Overuse of social media impacts mental health.",
            "It depends on how responsibly it is used."
        ])

    elif "learning" in topic:
        return random.choice([
            "Online learning is flexible but lacks interaction.",
            "Offline learning improves engagement.",
            "Hybrid learning seems most effective."
        ])

    elif "education" in topic:
        return random.choice([
            "Free education improves accessibility.",
            "Funding quality education is challenging.",
            "Affordable education is more realistic."
        ])

    elif "technology" in topic:
        return random.choice([
            "Technology improves life but reduces activity.",
            "Balance is key in using technology.",
            "Overuse can make people less productive."
        ])

    return random.choice([
        "That's a valid point.",
        "I agree to some extent.",
        "Can you elaborate further?"
    ])