import os
import requests
from backend.core.config import get_settings

settings = get_settings()

def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {settings.LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(settings.LLM_ENDPOINT, headers=headers, json=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("LLM API Error:", response.status_code, response.text)
        raise e
    return response.json()["choices"][0]["message"]["content"]
