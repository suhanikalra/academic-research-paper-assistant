# agents/future_works_agent.py
import requests

OLLAMA_API_URL = "http://localhost:11434/v1/generate"

def generate_future_works(context: str):
    prompt = f"Given the following research, suggest potential future research opportunities:\n{context}"
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Error with Ollama API: {response.status_code} - {response.text}")
