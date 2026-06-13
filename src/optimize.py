import vectorbt as vbt 

def test_ma_strategy(df, ma_period):
    close = df["Close"]
    ma = (close.rolling(ma_period).mean())
    entries = close > ma
    exits = close < ma
    
    portfolio = vbt.Portfolio.from_signals(close, entries, exits, init_cash=10000, freq='1D')
    
    return {"MA": ma_period,

            "Return":
            portfolio.total_return().item(),

            "Sharpe":
            portfolio.sharpe_ratio().item(),

            "Drawdown":
            portfolio.max_drawdown().item(),
    }

def optimize_strategy(df):
    periods = [
        20, 50, 100, 150, 200
    ]
    results = []

    for period in periods:
        result = test_ma_strategy(df, period)
        results.append(result)

    return results

    