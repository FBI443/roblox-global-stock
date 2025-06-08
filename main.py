import requests
import time
import json

# 🛠️ CONFIGURAÇÕES
API_KEY = "SUA_API_KEY_DA_ROBLOX"
UNIVERSE_ID = "SEU_UNIVERSE_ID"
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
