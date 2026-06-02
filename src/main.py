from fetch_data import get_nifty_data
from metrics import (
    fifty_two_week_high, 
    fifty_two_week_low , 
    annualized_volatility,
    moving_averages,
    latest_close,
    vix_regime,
    market_regime
)
from fetch_vix import get_vix_data


nifty = get_nifty_data()
high = fifty_two_week_high(nifty)
low = fifty_two_week_low(nifty)
volatility = annualized_volatility(nifty)

dma20 = moving_averages(nifty, 20)
dma50 = moving_averages(nifty, 50)
dma200 = moving_averages(nifty, 200)


print(f"25 Week High : {high:.2f}")
print(f"25 Week Low : {low:.2f}")
print(f"Anuallized Volatility :  {volatility:.2f}%")

print(f"20 DMA  : {dma20:.2f}")
print(f"50 DMA  : {dma50:.2f}")
print(f"200 DMA : {dma200:.2f}")

vix = get_vix_data()
current_vix = latest_close(vix)


fear_level = vix_regime(current_vix)


current_price = nifty["Close"].iloc[-1].item()

regime = market_regime(current_price, dma200)



print("\nMARKET SUMMARY")
print("-" * 30)

print(f"Nifty Price    : {current_price:.2f}")
print(f"India VIX      : {current_vix:.2f}")
print(f"Fear Level     : {fear_level}")
print(f"Market Regime  : {regime}")