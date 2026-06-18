import pandas as pd 

def future_returns(prices, days):
    return (prices.shift(-days)/prices-1)*100

def classify_vix(vix):
    if vix < 15:
        return "LOW"

    elif vix < 20:
        return "NORMAL"

    elif vix < 30:
        return "HIGH"

    return "EXTREME"

# preparing data set

def prepare_dataset(nifty, vix):
    df = pd.DataFrame()
    
    df['Nifty'] = nifty["Close"]
    df['VIX'] = vix["Close"]
    df["5D"] = future_returns(df["Nifty"], 5)
    df["20D"] = future_returns(df["Nifty"], 20)
    df["60D"] = future_returns(df["Nifty"], 60)

    df["Regime"] = (df["VIX"].apply(classify_vix))
    
    return df

# analyse regime

def analyse_regime(df):

    result=(df.groupby("Regime") [["5D", "20D", "60D"]].mean())
    return result

