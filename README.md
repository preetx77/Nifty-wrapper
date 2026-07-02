# NIFTY Research Lab

A hypothesis-driven quantitative research framework for studying the Indian equity market.

Instead of building another technical indicator dashboard, this project focuses on testing market hypotheses using historical data, event studies, forward return analysis, and systematic validation.

The goal is to answer questions such as:

- Does market fear create future opportunity?
- Do deep drawdowns historically recover faster?
- Does trend persistence actually exist?
- Can market states be quantified rather than guessed?

---

## Motivation

Most retail trading systems begin with an indicator and search for confirmation.

This project follows the opposite workflow.

```
Observation
      ↓
Hypothesis
      ↓
Historical Data
      ↓
Statistical Analysis
      ↓
Forward Return Measurement
      ↓
Conclusion
```

Every module is built to test a market hypothesis rather than generate arbitrary trading signals.

---

## Research Questions Explored

### Volatility Regimes

> What happens to NIFTY after different India VIX regimes?

Measures forward returns after:

- Low VIX
- Normal VIX
- High VIX

---

### Trend Persistence

> Does trading above the 200 DMA actually improve future returns?

Compares forward performance when NIFTY trades:

- Above 200 DMA
- Below 200 DMA

---

### Drawdown Recovery

> Do larger market corrections lead to stronger recoveries?

Classifies drawdowns into:

- None
- Mild
- Moderate
- Severe

Then measures:

- 20-Day Forward Return
- 60-Day Forward Return
- 120-Day Forward Return

---

### Drawdown Distribution Analysis

Instead of relying only on averages, the framework evaluates:

- Sample Size
- Mean
- Median
- Standard Deviation
- Best Recovery
- Worst Recovery

This helps determine whether an apparent edge is broad-based or driven by a few outliers.

---

## Current Capabilities

### Market Analytics

- NIFTY 50 Market Summary
- India VIX Monitoring
- Annualized Volatility
- 52 Week High / Low
- Moving Averages (20 / 50 / 200 DMA)
- Market Regime Classification

---

### Breadth Analysis

Measures internal market participation using:

- Stocks Above 50 DMA
- Breadth Strength Classification

---

### Correlation Analysis

Studies the relationship between:

- NIFTY Returns
- India VIX Returns

Includes:

- Daily Correlation
- Rolling Correlation
- Correlation Regime Detection

---

### Strategy Research

Includes:

- Signal Generation
- Historical Backtesting
- Walk Forward Validation
- Strategy Optimization

Performance is evaluated using:

- Total Return
- Sharpe Ratio
- Sortino Ratio
- Calmar Ratio
- Profit Factor
- Drawdown
- Win Rate

---

## Project Structure

```
finance/
│
├── data/
│
├── research/
│   ├── core/
│   │   ├── future_returns.py
│   │   ├── regimes.py
│   │   ├── statistics.py
│   │   └── utils.py
│   │
│   ├── studies/
│   │   ├── vix.py
│   │   ├── trend.py
│   │   ├── drawdown.py
│   │   ├── breadth.py
│   │   └── correlation.py
│   │
│   └── reports/
│
├── src/
│   ├── main.py
│   ├── fetch_data.py
│   ├── fetch_vix.py
│   ├── metrics.py
│   ├── backtest.py
│   ├── optimize.py
│   ├── walkforward.py
│   ├── signals.py
│   └── visualize.py
│
└── README.md
```

---

## Example Output

```
============================================================
NIFTY 50 MARKET ANALYSIS
============================================================

Market Summary
Market Breadth
Volatility Analysis
Correlation Analysis
Trading Signal
Backtest Results
Walk Forward Validation

============================================================
Research Studies
============================================================

VIX Regime Study
Trend Persistence Study
Drawdown Recovery Study
Drawdown Distribution Analysis
```

---

## Tech Stack

- Python
- Pandas
- NumPy
- yfinance
- VectorBT
- Matplotlib

---

## Current Findings

Some observations from the current research:

- Higher market stress has often been followed by stronger medium-term recoveries.
- Trading below the 200 DMA did not consistently underperform within the tested sample.
- Moderate drawdowns showed stronger forward returns than normal market conditions.
- Walk-forward validation highlighted that simple moving-average strategies failed to generalize, reinforcing the need for robust out-of-sample testing.

These findings are descriptive rather than predictive and require testing over longer historical periods before drawing strong conclusions.

---

## Roadmap

Planned research modules:

- Stress Recovery Framework (Drawdown × VIX)
- Breadth Persistence Analysis
- Distance-from-Trend Studies
- Cross-Asset Research (USDINR, Gold, S&P 500)
- Statistical Significance Testing
- Bootstrap Validation
- Probability-Based Market State Engine

---

## Disclaimer

This project is intended for quantitative research and educational purposes.

It is **not** an automated trading system and should not be interpreted as investment advice.

The emphasis is on understanding market behaviour through data rather than predicting prices.

---

## Author

**Preet Sonar**

Computer Science Undergraduate | Quantitative Finance & Data Research

GitHub: https://github.com/preetx77
