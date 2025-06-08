import requests
import time
import json

# 🛠️ CONFIGURAÇÕES
API_KEY = "dPvOv5mj3Um5Lw0ZNo00sbs5izh685T0vyEIVAR0VsWPHIDRZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkluTnBaeTB5TURJeExUQTNMVEV6VkRFNE9qVXhPalE1V2lJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaVlYTmxRWEJwUzJWNUlqb2laRkIyVDNZMWJXb3pWVzAxVEhjd1drNXZNREJ6WW5NMWFYcG9OamcxVkRCMmVVVkpWa0ZTTUZaelYxQklTVVJTSWl3aWIzZHVaWEpKWkNJNklqRTJPVE01TnpZd0lpd2lZWFZrSWpvaVVtOWliRzk0U1c1MFpYSnVZV3dpTENKcGMzTWlPaUpEYkc5MVpFRjFkR2hsYm5ScFkyRjBhVzl1VTJWeWRtbGpaU0lzSW1WNGNDSTZNVGMwT1RReU9UY3dOeXdpYVdGMElqb3hOelE1TkRJMk1UQTNMQ0p1WW1ZaU9qRTNORGswTWpZeE1EZDkuTzE4N0IxTFVvVXhBN1FndWtkLUJPV2NXaUhsd004Uk81ZzdkNmh4eWJnTFM2MGw2YmJJYTI4NjlhcTRJUGE4MThvOUtQSm00TF9kcXVhWjFlUUtjMHJhMWpmUExCWUZFZ3FzZ0RrdXhYODR2akRIVFpGRjR6STR3NHJhdUFYV2huN19BYW5XVHAxUWhmZWRZRnZpVGx3OHNMQV92V0dyd2VaQVROSTA4RmItMFZpcXVMRXhIYjRPMXpmYUlTOGFINjlzdlFPdkZiWU1SVUhZcnZnQ2E1d3J0eWJnRnB4OWZQRmxSVXEyZmZ4Z3dLQmJKaDRiZzRwR3FVVmt6cWp2N19kUHpnR3h4SklGLTdRVVRWWlhtRFkxRXJhTGRWUE1lWkxnMzlBYjJKNUpLY2N2QzdqMlVnODlqTGxpb28yczNuZnpYMFVfNEN1eU5aMENvTS1LN1BR"
UNIVERSE_ID = "7502906864"
DATASTORE_NAME = "GlobalStock"
ENTRY_KEY = "MainStock"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

BASE_URL = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries/entry?datastoreName={DATASTORE_NAME}&entryKey={ENTRY_KEY}"

def atualizar_estoque():
    estoque = {
        "Espadas": 15,
        "Poções": 8,
        "Flechas": 52
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(estoque))
    print(f"[POST] Código {response.status_code} - {response.text}")

def ler_estoque():
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        dados = response.json()
        print(f"[GET] Estoque atual: {json.dumps(dados, indent=2)}")
    else:
        print(f"[GET] Erro: {response.status_code} - {response.text}")

def loop():
    while True:
        print("\n🔄 Ciclo iniciado...")
        atualizar_estoque()
        ler_estoque()
        print("🕒 Aguardando 60 segundos...\n")
        time.sleep(60)

if __name__ == "__main__":
    loop()
