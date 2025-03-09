import requests
import json

# Define Ollama server URL
OLLAMA_URL = "http://10.1.1.9:11434/api/generate"

# Define request payload
payload = {
    "model": "llama3:8b-instruct-q8_0",  # Change to the desired model (e.g., "llama3", "gemma", etc.)
    "prompt": "Hi",
    "stream": False  # Set to True if you want streamed responses
}

# Send the POST request
response = requests.post(OLLAMA_URL, data=json.dumps(payload))

# Check for a successful response
if response.status_code == 200:
    result = response.json()
    print("Response:", result["response"])
else:
    print("Error:", response.status_code, response.text)
