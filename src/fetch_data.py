import yfinance as yf
from datetime import datetime

def fetch_crypto_data(ticker='BTC-USD', start_date='2021-01-01', end_date=None):
    if end_date is None:
        end_date = datetime.today().strftime('%Y-%m-%d')

    df = yf.download(ticker, start=start_date, end=end_date)

    # ✅ Date sütunu index olarak yazılır, ama CSV'ye sütun olarak da eklenir
    df.reset_index(inplace=True)

    # ✅ Gereksiz satır başlıkları olmadan kayıt
    df.to_csv(f'data/{ticker}.csv', index=True)  # index=True olmadan tarih kaybolur!

    print(f"✅ {ticker} verisi 'data/{ticker}.csv' dosyasına kaydedildi.")
    return df
