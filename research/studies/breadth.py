import yfinance as yf 

from src.nifty50 import NIFTY50 
from src.metrics import ( 
    moving_averages,
    is_above_dma
)

def breadth_analysis():

    above_50dma = 0
    total = len(NIFTY50)

    for stock in NIFTY50:
        try:
            df = yf.download(
                stock,
                period='1y',
                auto_adjust=True,
                progress=False
            )

            if df.empty:
                print(f"{stock} has no data")
                continue

            current_price = (
                df["Close"].iloc[-1].item()
            )
            dma50 = moving_averages(df, 50)

            if is_above_dma(
                current_price, dma50
            ):

                above_50dma +=1

            print(
                f"{stock}"
                f" | Price: {current_price:.2f}"
                f" | 50DMA: {dma50:.2f}"
            )
            print(
                is_above_dma(
                    current_price,
                    dma50
                )
            )
        except Exception as e:
            print(f"Error processing {stock}... skipping")

    return above_50dma, total

def breadth_strength(score):

    percentage = (
        score * 100
    )

    if percentage > 70:
        return "STRONG"

    elif percentage > 40:
        return "NEUTRAL"

    return "WEAK"
    