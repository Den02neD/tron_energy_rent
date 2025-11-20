import requests, json

def get_tron_price():
    return requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd").json()["tron"]["usd"]

def estimate_rent(cost_trx):
    url = "https://api.trongrid.io/wallet/triggerconstantcontract"
    payload = {
        "owner_address": "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb",
        "contract_address": "TRXbY8c3fJ6z5hnNinGJ3vKzx9L3iXgKvs",
        "function_selector": "rentEnergy(uint64,uint64)",
        "parameter": "0000000000000000000000000000000000000000000000000000000000000001,0000000000000000000000000000000000000000000000000000000000989680",
        "fee_limit": 1000000
    }
    r = requests.post(url, json=payload).json()
    energy = int(r["constant_result"][0], 16) // 1000000
    print(f"За {cost_trx} TRX можно арендовать ~{energy:,} energy на 30 дней")
    print(f"Цена 1M energy ≈ ${(cost_trx / energy * 1_000_000 / get_tron_price()):.2f}")

if __name__ == "__main__":
    trx = float(input("Сколько TRX готов потратить? "))
    estimate_rent(trx)
