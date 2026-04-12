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
            ("Opponent", "You disagree politely and provide counter-arguments."),
            ("Neutral", "You balance both sides and give a thoughtful perspective.")
        ]

        role_name, role_prompt = roles[turn % len(roles)]

        prompt = f"""
        {role_prompt}

        Topic: {topic}

        Previous speaker said: "{user_input}"

        Respond as a {role_name} in a group discussion.
        Make your response:
        - Relevant to the topic
        - Different from previous responses
        - Natural and conversational
        - 1–2 sentences only
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
            "AI is transforming jobs, but it also creates new opportunities.",
            "Human creativity still gives us an advantage over AI.",
            "Automation may replace routine tasks, not complex roles."
        ])

    elif "social media" in topic:
        return random.choice([
            "Social media connects people but can also distract them.",
            "It has benefits, but overuse affects mental health.",
            "Responsible usage is the key."
        ])

    elif "learning" in topic:
        return random.choice([
            "Online learning is flexible but lacks interaction.",
            "Offline learning builds discipline.",
            "A hybrid model works best."
        ])

    elif "education" in topic:
        return random.choice([
            "Free education improves access.",
            "Funding quality is a challenge.",
            "Affordable education is more realistic."
        ])

    elif "technology" in topic:
        return random.choice([
            "Technology improves life but can reduce activity.",
            "Balance is important.",
            "Overuse leads to laziness."
        ])

    return random.choice([
        "That's an interesting point.",
        "I see your perspective.",
        "Can you explain more?"
    ])