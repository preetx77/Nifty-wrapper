import pandas as pd

def market_state(price, dma):
    if price > dma:
        return "ABOVE 200"

    return "BELOW 200"

def future_returns(prices, days):
    return(prices.shift(-days)/ prices - 1) * 100

def prepare_trend_dataset(nifty):

    df =pd.DataFrame()
    df["Close"] = nifty["Close"]
    df["DMA200"] = (nifty["Close"].rolling(200).mean())

    df["5D"] = future_returns(df["Close"],5)
    df["20D"] = future_returns(df["Close"],20)
    df["60D"] = future_returns(df["Close"], 60)
    df["State"] = df.apply(lambda row:market_state(row["Close"], row["DMA200"]),axis = 1)
    return df.dropna()


def analyze_trend(df):

    print("\nOBSERVATIONS")
    print(df["State"].value_counts())

    return (df.groupby("State")[["5D","20D","60D"]].mean())