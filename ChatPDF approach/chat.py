import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CHATPDF_API_KEY")
print(api_key)

headers = {
    'x-api-key': api_key,
    "Content-Type": "application/json",
}

# tam src: src_f6JtID1k9nZX20im5xFA9, client-reqs src: src_kBcRi75xc7EKQ85g9Gze9
# data = {
#     "referenceSources": True,
#     'sourceId': "src_kBcRi75xc7EKQ85g9Gze9",
#     'messages': [
#         {
#             'role': "user",
#             'content': "Wyeksportuj informacje na temat wymagań klienta wobec firmy.",
#         }
#     ]
# }

# response = requests.post(
#     'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

# if response.status_code == 200:
#     print('Result:', response.json()['content'])
# else:
#     print('Status:', response.status_code)
#     print('Error:', response.text)
    
    
    
data = {
    "referenceSources": True,
    'sourceId': "src_f6JtID1k9nZX20im5xFA9",
    'messages': [
        {
            'role': "user",
            'content': "Wyślę Ci zaraz informacje na temat wymagań klienta. Ty, na ich podstawie, spróbuj znaleźć w dokumencie takie usługi, które spełniają wymagania klienta (Offer + Documentation). Gdy je znajdziesz, odeślij je. Wymagania klienta:  Zaprojektowanie, dostawę i wdrożenie zintegrowanego oprogramowania do kompleksowego inwentaryzowania zasobów pasywnych i aktywnych sieci i infrastruktury telekomunikacyjnej, wspierającego administrowanie zasobami sieci i infrastruktury telekomunikacyjnej ENEA Operator [P6]. Zapewnienie gwarancji serwisu na całość prac związanych z wdrożeniem Systemu oraz dostarczone oprogramowanie na okres 36 miesięcy od daty podpisania protokołu odbioru końcowego [P10].                 Udzielanie wsparcia technicznego przy eksploatacji Systemu w języku polskim, możliwość zgłaszania wad, usterek i awarii w dni robocze w godzinach od 7:00 do 15:00 oraz prowadzenie i udostępnianie online rejestru zgłoszonych problemów [P10].                 Wymaganie, aby System spełniał wszystkie określone wymagania, takie jak interfejs użytkownika w polskiej wersji językowej, wewnętrzna integracja funkcjonalności Systemu, możliwość określania danych adresowych zgodnie z adresacją Teryt oraz posiadanie aktualnych danych słownikowych zgodnych z Teryt [P11].",
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