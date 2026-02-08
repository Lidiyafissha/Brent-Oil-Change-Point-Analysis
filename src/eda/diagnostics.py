import numpy as np
from statsmodels.tsa.stattools import adfuller

def compute_log_returns(df):
    if "Price" not in df.columns:
        raise ValueError("Price column missing")

    df = df.copy()
    df["log_return"] = np.log(df["Price"]).diff()
    return df.dropna()

def adf_test(series):
    result = adfuller(series)
    return {
        "adf_statistic": result[0],
        "p_value": result[1],
        "is_stationary": result[1] < 0.05
    }
