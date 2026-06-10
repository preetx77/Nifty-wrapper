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


def plot_vix(vix):
    plt.figure(figsize= (12,5))
    plt.plot(vix.index,vix["Close"], label = "India Vix")

    plt.title("INDIA VIX")
    plt.xlabel("Date")
    plt.ylabel("VIX")
    plt.grid(True)
    plt.legend()
    plt.show()

# rolling correlation chart
def plot_rolling_correaltion(rolling_corr):
    plt.figure(figsize=(12, 5))
    plt.plot(rolling_corr.index, rolling_corr, label="Rolling Correlation")
    plt.axhline(y=0, linestyle="--")
    plt.title("NIFTY vs VIX correaltion")
    plt.xlabel("Date")
    plt.ylabel("Correaltion")
    plt.grid(True)
    plt.legend()
    plt.show()

    
