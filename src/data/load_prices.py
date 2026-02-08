import pandas as pd
from pathlib import Path

def load_price_data(filepath: str) -> pd.DataFrame:
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Price data not found at {filepath}")

    df = pd.read_csv(path)

    required_cols = {"Date", "Price"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {required_cols}")

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y", errors="coerce")

    if df["Date"].isnull().any():
        raise ValueError("Date parsing failed for some rows.")

    df = df.sort_values("Date").reset_index(drop=True)
    return df
