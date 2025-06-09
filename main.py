
import requests
import json
import time

# CONFIGURAÇÃO
API_KEY = "dPvOv5mj3Um5Lw0ZNo00sbs5izh685T0vyEIVAR0VsWPHIDRZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkluTnBaeTB5TURJeExUQTNMVEV6VkRFNE9qVXhPalE1V2lJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaVlYTmxRWEJwUzJWNUlqb2laRkIyVDNZMWJXb3pWVzAxVEhjd1drNXZNREJ6WW5NMWFYcG9OamcxVkRCMmVVVkpWa0ZTTUZaelYxQklTVVJTSWl3aWIzZHVaWEpKWkNJNklqRTJPVE01TnpZd0lpd2lZWFZrSWpvaVVtOWliRzk0U1c1MFpYSnVZV3dpTENKcGMzTWlPaUpEYkc5MVpFRjFkR2hsYm5ScFkyRjBhVzl1VTJWeWRtbGpaU0lzSW1WNGNDSTZNVGMwT1RReU9UY3dOeXdpYVdGMElqb3hOelE1TkRJMk1UQTNMQ0p1WW1ZaU9qRTNORGswTWpZeE1EZDkuTzE4N0IxTFVvVXhBN1FndWtkLUJPV2NXaUhsd004Uk81ZzdkNmh4eWJnTFM2MGw2YmJJYTI4NjlhcTRJUGE4MThvOUtQSm00TF9kcXVhWjFlUUtjMHJhMWpmUExCWUZFZ3FzZ0RrdXhYODR2akRIVFpGRjR6STR3NHJhdUFYV2huN19BYW5XVHAxUWhmZWRZRnZpVGx3OHNMQV92V0dyd2VaQVROSTA4RmItMFZpcXVMRXhIYjRPMXpmYUlTOGFINjlzdlFPdkZiWU1SVUhZcnZnQ2E1d3J0eWJnRnB4OWZQRmxSVXEyZmZ4Z3dLQmJKaDRiZzRwR3FVVmt6cWp2N19kUHpnR3h4SklGLTdRVVRWWlhtRFkxRXJhTGRWUE1lWkxnMzlBYjJKNUpLY2N2QzdqMlVnODlqTGxpb28yczNuZnpYMFVfNEN1eU5aMENvTS1LN1BR"
UNIVERSE_ID = "7502906864"
DATASTORE_NAME = "GlobalStock"
ENTRY_KEY = "MainStock"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

URL = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries/entry?datastoreName={DATASTORE_NAME}&entryKey={ENTRY_KEY}"

# Leitura dos dados locais
def carregar_dados():
    with open("seeds.json", "r") as f:
        seeds = json.load(f)
    with open("variants.json", "r") as f:
        variants = json.load(f)
    return seeds, variants

# Geração de estoque com base nas sementes
def gerar_estoque(seeds):
    estoque = {}
    for nome, semente in seeds.items():
        from random import randint
        chance_ok = randint(semente["ChanceMin"], semente["ChanceMax"]) == randint(semente["ChanceMin"], semente["ChanceMax"])
        if chance_ok:
            quantidade = randint(semente["QuantityMin"], semente["QuantityMax"])
        else:
            quantidade = 0
        estoque[nome] = {
            "Quantity": quantidade,
            "Price": semente["Sheckles"],
            "Activated": semente.get("Activated", True)
        }
    return estoque

def enviar_para_open_cloud(dados):
    res = requests.post(URL, headers=HEADERS, json=dados)
    print(f"[POST] Código {res.status_code} - {res.text}")

def loop():
    while True:
        print("🔄 Atualizando estoque global...")
        seeds, variants = carregar_dados()
        estoque = gerar_estoque(seeds)
        enviar_para_open_cloud(estoque)
        print("✅ Estoque atualizado com sucesso. Aguardando 60s...")
        time.sleep(60)

if __name__ == "__main__":
    loop()
