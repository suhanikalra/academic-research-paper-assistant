# agents/qa_agent.py
import requests

# Ensure the API endpoint and model name match your LLM setup
OLLAMA_API_URL = "http://localhost:11434/v1/ask"  # Replace with correct API URL if needed

def answer_question(context: str, question: str):
    payload = {
        "model": "llama2",  # Replace with your model name
        "question": question,
        "context": context
    }
    response = requests.post(OLLAMA_API_URL, json=payload)

    # Debugging: Print the status and response text for troubleshooting
    print("Q&A API Response Status:", response.status_code)
    print("Q&A API Response Text:", response.text)

    if response.status_code == 200:
        return response.json()  # Expecting JSON with an 'answer' key
    else:
        raise Exception(f"Error with Ollama API: {response.status_code} - {response.text}")
