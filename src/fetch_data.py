import yfinance as yf

def get_nifty_data():

    df = yf.download("^NSEI", period= "1y", auto_adjust=True)

    return df

if __name__ == "__main__":

    nifty = get_nifty_data()

    latest_price = nifty["Close"].iloc[-1].item()

    daily_return = (nifty["Close"].pct_change().iloc[-1].item()) * 100

    print(f"Latest Price : {latest_price:.2f}")
    print(f"Daily Return : {daily_return:.2f}%")

    nifty.to_csv("../data/nifty.csv")

    print("Data Saved Successfully ")