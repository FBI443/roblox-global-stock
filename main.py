
import requests
import json
import time

# CONFIGURAÇÃO
API_KEY = "SUA_API_KEY"
UNIVERSE_ID = "SEU_UNIVERSE_ID"
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
