# src/live_price.py

import requests

def get_live_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print("❌ Canlı fiyat alınamadı:", e)
        return None
