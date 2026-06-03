def fifty_two_week_high(df):
    return df["High"].max().item()


def fifty_two_week_low(df):
    return df["Low"].min().item()


def annualized_volatility(df):
    returns = df["Close"].pct_change()

    volatility = (
        returns.std().item()
        * (252 ** 0.5)
        * 100
    )
    return volatility

def moving_averages(df, days):
    return (df["Close"].rolling(days).mean().iloc[-1].item())

def latest_close(df):
    return df["Close"].iloc[-1].item()


def vix_regime(vix):

    if vix < 15:
        return "LOW FEAR"
    elif vix < 20:
        return "NORMAL"
    elif vix < 20:
        return "HIGH FEAR"
    return "PANIC"

def market_regime(current_price, dma200):

    if current_price > dma200:
        return "BULL MARKET"
    
    return "BEAR MARKET"

# for nifty 50
def is_above_dma(current_price, dma):
    return current_price > dma

    
