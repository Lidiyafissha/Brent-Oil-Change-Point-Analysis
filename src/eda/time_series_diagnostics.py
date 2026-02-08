import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
data_path = os.path.join(project_root, "data", "raw", "BrentOilPrices.csv")

df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")
df = df.sort_values("Date")

# Plot raw prices
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Price"])
plt.title("Brent Oil Prices Over Time")
plt.xlabel("Date")
plt.ylabel("USD per Barrel")
plt.show()

# Log returns
df["log_return"] = np.log(df["Price"]).diff()

# Plot log returns
plt.figure(figsize=(12,4))
plt.plot(df["Date"], df["log_return"])
plt.title("Log Returns of Brent Oil Prices")
plt.xlabel("Date")
plt.ylabel("Log Return")
plt.show()

# Stationarity test
log_returns = df["log_return"].dropna()
adf_result = adfuller(log_returns)

print("ADF Statistic:", adf_result[0])
print("p-value:", adf_result[1])
