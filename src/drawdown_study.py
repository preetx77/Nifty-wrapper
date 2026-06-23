import pandas as pd

def future_returns(prices, days):
    return (prices.shift(-days) / prices - 1)*100

def calculate_drawdown(prices):

    rolling_peak = prices.cummax()
    drawdown = (prices - rolling_peak) / rolling_peak * 100

    return drawdown

# ----- drawdown regimes------------

def classify_drawdown(dd):
    
    if dd <= -15:
        return "SEVERE"
    
    elif dd <= -10:
        return "MODERATE"
    
    elif dd <= -5:
        return "MILD"

    return "NONE"

#---------- dataset --------------

def prepare_drawdown_dataset(nifty):
    df = pd.DataFrame()

    df["Close"] = nifty["Close"]
    df["Drawdown"] = calculate_drawdown(df["Close"])
    
    df["20D"] = future_returns(df["Close"], 20)
    df["60D"] = future_returns(df["Close"], 60)
    df["120D"]= future_returns(df["Close"], 120)
    df["Regime"] = (df["Drawdown"].apply(classify_drawdown))

    return df.dropna()


# ------------- anaysis function ------------

def analyse_drawdown(df):
    print("\n OBSERVATIONS")
    print(df["Regime"].value_counts())
    return(df.groupby("Regime")[["20D","60D", "120D"]].mean())

