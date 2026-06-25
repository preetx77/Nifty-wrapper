# NIFTY 50 Market Analysis & Trading System

A Python-based tool for analyzing the Indian stock market (NIFTY 50) using technical indicators, correlation analysis, and backtesting strategies.

---

## 📋 What This Project Does

This system analyzes market trends and generates trading signals by:
- Fetching real-time market data (NIFTY 50 index & India VIX)
- Calculating key technical indicators (moving averages, volatility, breadth)
- Analyzing market regimes and fear levels
- Backtesting trading strategies
- Optimizing strategy parameters
- Evaluating drawdown recovery patterns

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Analysis
```bash
cd src
python main.py
```

---

## 📁 Project Structure

```
finance/
├── src/
│   ├── main.py                 # Entry point - runs complete analysis
│   ├── fetch_data.py           # Downloads NIFTY & VIX data
│   ├── fetch_vix.py            # VIX data fetching
│   ├── metrics.py              # Technical indicators (volatility, moving averages)
│   ├── breadth.py              # Market breadth analysis
│   ├── correlation.py          # NIFTY-VIX correlation analysis
│   ├── signals.py              # Trading signal generation
│   ├── backtest.py             # Backtesting engine
│   ├── optimize.py             # Strategy parameter optimization
│   ├── walkforward.py          # Walk-forward testing
│   ├── visualize.py            # Charts & plots
│   ├── vix_study.py            # VIX regime analysis
│   ├── trend_study.py          # Trend persistence research
│   ├── drawdown_study.py       # Drawdown analysis
│   ├── drawdown_v2.py          # Enhanced drawdown analysis
│   ├── nifty50.py              # NIFTY 50 ticker list
│   └── research.py             # Research utilities
├── data/
│   └── nifty.csv              # Cached NIFTY 50 data
└── requirements.txt            # Python dependencies
```

---

## 📊 Key Features

### Market Indicators
- **Volatility**: Annualized volatility & 52-week high/low
- **Trend**: 200-day moving average, above/below trend states
- **Fear Level**: VIX-based fear classification (LOW/NORMAL/HIGH/PANIC)
- **Market Regime**: Bull or Bear market classification

### Breadth Analysis
- Percentage of stocks trading above 50-day MA
- Breadth strength rating (STRONG/NEUTRAL/WEAK)

### Correlation Study
- NIFTY-VIX correlation tracking
- 30-day rolling correlation
- Correlation regimes (PANIC/RISK-OFF/NORMAL/DISCONNECTED)

### Backtesting & Optimization
- Strategy backtesting with performance metrics
- Parameter optimization (moving average periods)
- Walk-forward validation
- Drawdown analysis & recovery metrics

### Research Modules
- **VIX Study**: Regime analysis during different market conditions
- **Trend Study**: Returns analysis based on trend persistence
- **Drawdown Study**: Recovery time after drawdowns

---

## 📈 Sample Output

```
MARKET SUMMARY
------------------------------
Nifty Price    : 23,150.45
India VIX      : 14.25
Fear Level     : NORMAL
Market Regime  : BULL MARKET

MARKET BREADTH
------------------------------
Stocks Above 50 DMA : 28/50
Breadth Strength    : STRONG

NIFTY <-> VIX CORRELATION
------------------------------
Correlation : -0.85
30 DAY ROLLING CORRELATION: -0.78
Correlation Regime : PANIC CORRELATION

TRADING SIGNAL
------------------------------
Signal : BUY
```

---

## 🔧 How to Use

### Run Full Analysis
```bash
python main.py
```

### Run Individual Analysis
```python
from fetch_data import get_nifty_data, get_vix_data
from metrics import annualized_volatility, moving_averages

nifty = get_nifty_data()
vol = annualized_volatility(nifty)
dma200 = moving_averages(nifty, 200)
```

### Backtest a Strategy
```python
from backtest import run_backtest
portfolio = run_backtest(nifty)
print(portfolio.stats())
```

### Optimize Strategy Parameters
```python
from optimize import optimize_strategy
results = optimize_strategy(nifty)
for result in results:
    print(f"MA: {result['MA']} | Sharpe: {result['Sharpe']:.2f}")
```

---

## 📦 Requirements

- Python 3.8+
- yfinance (data fetching)
- pandas (data processing)
- numpy (calculations)
- matplotlib (plotting)

See `requirements.txt` for full list.

---

## 🎯 Use Cases

- **Day Traders**: Real-time market signals and breadth analysis
- **Swing Traders**: Trend identification and strategy backtesting
- **Researchers**: Market correlation and regime analysis
- **Portfolio Managers**: Drawdown metrics and risk assessment

---

## 📝 Notes

- Data is fetched from Yahoo Finance (real-time)
- NIFTY data: 5-year history
- VIX data: 1-year history
- Results cached in `data/nifty.csv`

---

## 📞 Contact

For questions or suggestions, review the code in `src/main.py` for workflow overview.
