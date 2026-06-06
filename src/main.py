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
from breadth import (
    breadth_analysis,
    breadth_strength
)
from correlation import ( daily_returns, correlation, rolling_correlation, rolling_regime)


nifty = get_nifty_data()
high = fifty_two_week_high(nifty)
low = fifty_two_week_low(nifty)
volatility = annualized_volatility(nifty)

dma20 = moving_averages(nifty, 20)
dma50 = moving_averages(nifty, 50)
dma200 = moving_averages(nifty, 200)


print(f"52 Week High : {high:.2f}")
print(f"52 Week Low : {low:.2f}")
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

above_50dma, total = breadth_analysis()

breadth_score = (
    above_50dma / total
)

strength = breadth_strength(
    breadth_score
)

print("\nMARKET BREADTH")
print("-" * 30)

print(
    f"Stocks Above 50 DMA : "
    f"{above_50dma}/{total}"
)

print(
    f"Breadth Strength    : "
    f"{strength}"
)

nifty_returns = daily_returns(nifty)
vix_returns = daily_returns(vix)
corr = correlation(nifty_returns,vix_returns)

rolling_corr = rolling_correlation(nifty_returns, vix_returns)
latest_rolling_corr = (rolling_corr.iloc[-1])

print("\nNIFTY ↔ VIX CORRELATION")
print("-" * 30)
print(f"Correlation : {corr:.2f}")

print("\n30 DAY ROLLING CORRELATION")
print("-" * 30)

print(f"Latest Rolling Corr : " f"{latest_rolling_corr:.2f}")

regime = rolling_regime(latest_rolling_corr)
print(f"Correlation Regime : " f"{regime}")