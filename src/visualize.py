import matplotlib.pyplot as plt

def plot_nifty_trend(df):
    plt.figure(figsize=(12, 6))

    plt.plot(df.index, df["Close"], label="Nifty")
    plt.plot(df.index, df["20DMA"], label="20 DMA")
    plt.plot(df.index, df["50DMA"], label="50 DMA")
    plt.plot(df.index, df["200DMA"], label="200 DMA")

    plt.title("NIFTY TREND ANALYSIS")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()