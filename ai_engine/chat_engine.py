import requests

# Ollama API
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"   # change to "llama3" for better quality


def get_ai_response(user_input):
    try:
        prompt = f"""
        You are a professional communication trainer.

        User said: {user_input}

        Respond clearly, helpfully, and encourage better communication.
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
            return fallback_response(user_input)

    except Exception:
        return fallback_response(user_input)


# 🔁 Fallback (if Ollama fails)
def fallback_response(user_input):
    return f"I understand your point about '{user_input}'. Can you explain it more clearly?"