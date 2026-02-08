import pandas as pd
from pathlib import Path

# Get the project root directory (parent of src/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "events2.csv"

def create_events_dataset():
    events = [
        ("1990-08-02", "Gulf War invasion of Kuwait", "Geopolitical Conflict"),
        ("1997-07-02", "Asian Financial Crisis", "Economic Shock"),
        ("2001-09-11", "9/11 attacks in the United States", "Geopolitical Shock"),
        ("2003-03-20", "US-led invasion of Iraq", "Geopolitical Conflict"),
        ("2008-09-15", "Global Financial Crisis", "Economic Shock"),
        ("2010-12-17", "Arab Spring begins", "Geopolitical Conflict"),
        ("2014-11-27", "OPEC decision not to cut production", "OPEC Policy"),
        ("2016-11-30", "OPEC production cut agreement", "OPEC Policy"),
        ("2020-03-11", "COVID-19 declared a pandemic", "Global Health Shock"),
        ("2020-04-20", "Oil price collapse due to demand crash", "Economic Shock"),
        ("2022-02-24", "Russia invades Ukraine", "Geopolitical Conflict"),
        ("2022-03-08", "Western sanctions on Russian oil", "Sanctions"),
    ]

    df = pd.DataFrame(events, columns=["date", "event", "category"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if df.isnull().any().any():
        raise ValueError("Event dataset contains invalid dates or missing values.")

    if len(df) < 10:
        raise ValueError("Event dataset must contain at least 10 events.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    return df

if __name__ == "__main__":
    create_events_dataset()

print("events2.csv saved successfully.")
