import matplotlib

matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt


def plot_price_data(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # 'Close' sütununu sayıya dönüştür
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='BTC/USD Close Price')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat (USD)')
    plt.title('Bitcoin Kapanış Fiyatı Zaman Serisi')
    plt.legend()
    plt.grid(True)
    plt.savefig('charts/price_chart.png')
    print("✅ price_chart.png dosyası charts klasörüne kaydedildi.")


def plot_returns_histogram(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # 'Close' sütununu sayıya dönüştür
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    df['Daily Return'] = df['Close'].pct_change()
    plt.figure(figsize=(10, 5))
    plt.hist(df['Daily Return'].dropna(), bins=50)
    plt.xlabel('Günlük Getiri')
    plt.ylabel('Frekans')
    plt.title('Günlük Getiriler Histogramı')
    plt.grid(True)
    plt.savefig('charts/returns_histogram.png')
    print("✅ returns_histogram.png dosyası charts klasörüne kaydedildi.")
