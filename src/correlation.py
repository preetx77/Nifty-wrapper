import pandas as pd


def daily_returns(df):

    returns = (
        df["Close"]
        .pct_change()
    )

    return returns


def correlation(series1, series2):

    merged = pd.concat([series1, series2],axis=1).dropna()
    corr = merged.iloc[:, 0].corr(merged.iloc[:, 1])

    return corr

def rolling_correlation(series1, series2, window=30):
    merged = (pd.concat([series1, series2], axis=1).dropna())
    rolling_corr = (merged.iloc[:, 0].rolling(window).corr(merged.iloc[:,1] ))
    
    return rolling_corr
