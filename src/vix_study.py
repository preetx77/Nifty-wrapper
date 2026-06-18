import pandas as pd 

def future_returns(prices, days):
    return (prices.shift(-days)/prices-1)*100
def classify_vix(vix):

    if pd.isna(vix):
        return None

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
    df = df.dropna(subset=["VIX"])
    return df

# analyse regime

def analyse_regime(df):

    grouped =df.groupby("Regime") 
    
    avg_returns = grouped[["5D", "20D", "60D"]].mean()
    counts = grouped.size()

    print("\n OBSERVATIONS")
    print(counts)

    return avg_returns

    print(df["VIX"].describe())
