# src/eda.py
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def compute_log_returns(df):
    df = df.copy()
    df["log_return"] = np.log(df["Price"]).diff()
    return df

def adf_test(series):
    result = adfuller(series.dropna())
    return {
        "ADF Statistic": result[0],
        "p-value": result[1]
    }
