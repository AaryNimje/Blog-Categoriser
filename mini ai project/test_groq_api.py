import requests
import os
from dotenv import load_dotenv
load_dotenv("api_key.env")
api_key = os.getenv("GROQ_API_KEY")

print(f"API key length: {len(api_key) if api_key else 0}")
print(f"API key first 5 chars: {api_key[:5] if api_key else 'None'}")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
}

try:
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data,
        timeout=10
    )
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {type(e).__name__} - {str(e)}")