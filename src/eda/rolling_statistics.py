import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
data_path = os.path.join(project_root, "data", "raw", "BrentOilPrices.csv")

df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
df = df.sort_values("Date")

df["rolling_mean"] = df["Price"].rolling(window=365).mean()
df["rolling_std"] = df["Price"].rolling(window=365).std()

plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Price"], alpha=0.5, label="Price")
plt.plot(df["Date"], df["rolling_mean"], label="Rolling Mean (1Y)")
plt.plot(df["Date"], df["rolling_std"], label="Rolling Std (1Y)")
plt.legend()
plt.title("Rolling Statistics of Brent Oil Prices")
plt.show()
