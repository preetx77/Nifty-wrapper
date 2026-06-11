import vectorbt as vbt 

def run_backtest(df):
    close = df["Close"].squeeze()
    dma200 = df["200DMA"].squeeze()

    entries = close > dma200
    exits = close < dma200

    portfoilio = vbt.Portfolio.from_signals(
        close=close, 
        entries=entries,
        exits=exits,
        init_cash=10000,
        freq='1D'
    )
    
    return portfoilio
