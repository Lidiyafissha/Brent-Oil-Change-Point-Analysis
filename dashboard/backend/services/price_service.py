import pandas as pd

DATA_PATH = "../../../data/raw/BrentOilPrices.csv"

def get_prices(start=None, end=None):
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])

    if start:
        df = df[df["Date"] >= start]
    if end:
        df = df[df["Date"] <= end]

    return df.to_dict(orient="records")
