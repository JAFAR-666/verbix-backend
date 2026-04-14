import requests

OLLAMA_URL = "https://abc123.ngrok-free.dev/api/generate"

def get_ai_response(user_input):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi",
                "prompt": f"""
You are a communication coach.

Respond clearly, naturally, and helpfully.

User: {user_input}
AI:
""",
                "stream": False
            },
            timeout=60
        )

        data = response.json()
        print("CHAT DEBUG:", data)

        return data.get("response", "No response from AI")

    except Exception as e:
        print("CHAT ERROR:", e)
        return "AI not responding"