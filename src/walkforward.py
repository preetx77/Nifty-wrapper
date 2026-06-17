import vectorbt as vbt 

def split_data(df):

    split_index = int(len(df) * 0.7)

    train = df.iloc[:split_index]

    test = df.iloc[split_index:]

    return train, test

def backtest_ma(df,ma_period):

    close = df["Close"]

    ma = (close.rolling(ma_period).mean())

    entries = close > ma

    exits = close < ma

    portfolio = vbt.Portfolio.from_signals(
        close,
        entries,
        exits,
        init_cash=10000,
        freq="1D"
    )

    return portfolio

def walk_forward_test(df):

    train, test = split_data(df)

    train_pf = backtest_ma(train,20  )

    test_pf = backtest_ma(test,20)

    return train_pf, test_pf