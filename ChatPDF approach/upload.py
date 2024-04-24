import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CHATPDF_API_KEY")
print(api_key)

files = [
    ('file', ('file', open('Investments-paper.pdf', 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': api_key
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)