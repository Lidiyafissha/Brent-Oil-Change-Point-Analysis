# src/data_loader.py
import pandas as pd

def load_price_data(path):
    try:
        df = pd.read_csv(path)
        if "Date" not in df.columns or "Price" not in df.columns:
            raise ValueError("Required columns missing: Date, Price")

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
