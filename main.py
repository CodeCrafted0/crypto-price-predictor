from src.fetch_data import fetch_crypto_data
from src.preprocess import analyze_crypto_data
from src.model import train_price_model
from src.visualize import plot_price_data, plot_returns_histogram
from live_price import get_live_btc_price

# 1) Canlı fiyat
live_price = get_live_btc_price()
print(f"\n⚡ Canlı BTC/USD Fiyatı: {live_price:.2f} USD")

# 2) Veriyi indir
fetch_crypto_data('BTC-USD', start_date='2021-01-01')

# 3) Analiz yap
analyze_crypto_data('BTC-USD')

# 4) Model eğit
train_price_model('data/BTC-USD.csv')

# 5) Grafik çizimi
plot_price_data('data/BTC-USD.csv')
plot_returns_histogram('data/BTC-USD.csv')
