import pandas as pd

def analyze_crypto_data(ticker):
    df = pd.read_csv(f'data/{ticker}.csv', index_col='Date', parse_dates=True)

    # 🔧 String verileri sayıya çevir
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    returns = df['Close'].pct_change().dropna()

    print(f"📊 Günlük getiriler örneği:\n{returns.head()}")
