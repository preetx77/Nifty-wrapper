from src.fetch_data import get_nifty_data
from src.metrics import (
    fifty_two_week_high, 
    fifty_two_week_low , 
    annualized_volatility,
    moving_averages,
    latest_close,
    vix_regime,
    market_regime
)
from src.fetch_vix import get_vix_data
from research.studies.breadth import (
    breadth_analysis,
    breadth_strength
)
from research.studies.correlation import (daily_returns, correlation, rolling_correlation, rolling_regime)
from src.visualize import (plot_nifty_trend, plot_vix)
from src.signals import trading_signal
from src.backtest import run_backtest
from src.optimize import optimize_strategy
from src.walkforward import (walk_forward_test)
from research.studies.vix import (prepare_dataset, analyse_regime)
from research.studies.trend import (prepare_trend_dataset, analyze_trend)
from research.studies.drawdown import (prepare_drawdown_dataset, analyse_drawdown, drawdown_distribution)


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

print("\nNIFTY <-> VIX CORRELATION")
print("-" * 30)
print(f"Correlation : {corr:.2f}")

print("\n30 DAY ROLLING CORRELATION")
print("-" * 30)

print(f"Latest Rolling Corr : " f"{latest_rolling_corr:.2f}")

regime = rolling_regime(latest_rolling_corr)
print(f"Correlation Regime : " f"{regime}")

nifty["20DMA"] = (nifty["Close"].rolling(20).mean())
nifty["50DMA"] = (nifty["Close"].rolling(50).mean())
nifty["200DMA"] = (nifty["Close"].rolling(200).mean())

plot_nifty_trend(nifty)
# plot_rolling_correlation(rolling_corr)  # Commented out - function may not exist

# signal generation 
signal = trading_signal(current_price, dma200, current_vix, breadth_score)
print("\nTRADING SIGNAL")
print("-" * 30)
print(f"Signal : {signal}")

# backtesting engine 
portfoilio = run_backtest(nifty)
print("\n BACKTEST RESULTS")
print("-"* 30)
print(portfoilio.stats())

# optmizing strategy
results = optimize_strategy(nifty)

print("\n STRATEGY OPTIMIZATION")
print("-"*30)

for result in results:

    print(f"MA: {result['MA']} | "
        f"Return: {result['Return']:.2f} | "
        f"Sharpe: {result['Sharpe']:.2f} | "
        f"Drawdown: {result['Drawdown']:.2f}"
    )

# walkforward test 
train_pf, test_pf = (
    walk_forward_test(nifty)
)

print("\nWALK FORWARD TEST")
print("-" * 30)

print(
    f"Train Return : "
    f"{train_pf.total_return().iloc[0]:.2f}"
)

print(
    f"Test Return  : "
    f"{test_pf.total_return().iloc[0]:.2f}"
)

# ------------------------ vix research --------------------------------

research_df = prepare_dataset(nifty, vix)
results = analyse_regime(research_df)

print("\n VIX REGIME STUDY")
print("-" * 30)
print(results)

print("\n VIX STATISTICS")
print("-" * 30)
print(research_df["VIX"].describe())

print(research_df["Regime"].value_counts())
print(research_df[["VIX","Regime"]].head())

# -------------- trend study ---------------------------
trend_df = (prepare_trend_dataset(nifty))

trend_results = (analyze_trend(trend_df))

print("\nTREND PERSISTENCE STUDY")
print("-" * 30)

print(trend_results)

# --------------- Drawdown Study---------------------------

drawdown_df = (prepare_drawdown_dataset(nifty))
drawdown_results = (analyse_drawdown(drawdown_df))

print("\n DRAWDOWN RECOVERY STUDY")
print("-" * 50)

print(drawdown_results)

# ------------------- Drawdown V2 -----------------------------
v2_df = prepare_drawdown_dataset(nifty)
v2_results = drawdown_distribution(v2_df)

print("\n DRAWDOWN RECOVERY V2")
print("-" * 50)
print(v2_results)

