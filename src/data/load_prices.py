import pandas as pd
import os

# Load Brent oil price data
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
data_path = os.path.join(project_root, "data", "raw", "BrentOilPrices.csv")

df = pd.read_csv(data_path)

# Convert date column - use mixed format parsing
df["Date"] = pd.to_datetime(df["Date"], format="mixed", dayfirst=False)

# Sort by time
df = df.sort_values("Date").reset_index(drop=True)

# Basic checks
print(df.head())
print(df.info())
print(df.isna().sum())
