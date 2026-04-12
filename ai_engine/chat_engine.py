import requests

OLLAMA_URL = "https://flatly-agreeing-flyover.ngrok-free.dev/api/generate"

def get_ai_response(user_input):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi",
                "prompt": f"You are a communication coach. Give a helpful, clear, and relevant response.\nUser: {user_input}\nAI:",
                "stream": False
            },
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("response", "").strip() or "No response from AI"

        return f"AI Error: {response.status_code}"

    except Exception as e:
        return f"Error: {str(e)}"