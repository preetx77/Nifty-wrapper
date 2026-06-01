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