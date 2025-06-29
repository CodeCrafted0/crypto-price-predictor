# src/model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_price_model(csv_path):
    df = pd.read_csv(csv_path)

    # 🎯 Sadece sayısal değerleri kullan
    X = df[['Volume']].copy()
    y = df['Close'].copy()

    # 🧹 Hatalı satırları sil (string olabilir)
    X = X[pd.to_numeric(X['Volume'], errors='coerce').notnull()]
    y = y[X.index]

    X = X.astype(float)
    y = y.astype(float)

    # Model eğitimi
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print("\n🧠 Model Eğitimi Tamamlandı")
    print(f"📉 Ortalama Karesel Hata (MSE): {mse:.2f}")
