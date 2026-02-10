import pandas as pd

EVENTS_PATH = "../../../data/processed/events2.csv"

def get_events():
    df = pd.read_csv(EVENTS_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df.to_dict(orient="records")
