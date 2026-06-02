import yfinance as yf


def get_vix_data():

    df = yf.download(
        "^INDIAVIX",
        period="1y",
        auto_adjust=True
    )
    return df

if __name__ == "__main__":

    vix = get_vix_data()
    print(vix.tail())