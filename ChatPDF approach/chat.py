import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)

headers = {
    'x-api-key': api_key,
    "Content-Type": "application/json",
}

data = {
    "referenceSources": True,
    'sourceId': "src_XGuKc8IHKCqxPmqNnMsAP",
    'messages': [
        {
            'role': "user",
            'content': "Ile było aktywnych klientów w 2023 roku?",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)