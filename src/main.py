# ============================================================================
# MARKET ANALYSIS ORCHESTRATOR
# ============================================================================
# This file orchestrates the entire market analysis pipeline.
# Each function represents a distinct responsibility.
# No calculation logic here - only orchestration.
# ============================================================================

from src.fetch_data import get_nifty_data
from src.fetch_vix import get_vix_data
from src.metrics import (
    fifty_two_week_high,
    fifty_two_week_low,
    annualized_volatility,
    moving_averages,
    latest_close,
    vix_regime,
    market_regime,
)
from research.studies.breadth import breadth_analysis, breadth_strength
from research.studies.correlation import (
    daily_returns,
    correlation,
    rolling_correlation,
    rolling_regime,
)
from src.visualize import plot_nifty_trend, plot_vix
from src.signals import trading_signal
from src.backtest import run_backtest
from src.optimize import optimize_strategy
from src.walkforward import walk_forward_test
from research.studies.vix import prepare_dataset as vix_prepare_dataset, analyse_regime as vix_analyse_regime
from research.studies.trend import prepare_trend_dataset, analyze_trend
from research.studies.drawdown import (
    prepare_drawdown_dataset,
    analyse_drawdown,
    drawdown_distribution,
)


# ============================================================================
# INITIALIZATION
# ============================================================================

def initialize_market():
    """Fetch market data once at startup."""
    nifty = get_nifty_data()
    vix = get_vix_data()
    return nifty, vix


# ============================================================================
# PIPELINE FUNCTIONS
# ============================================================================

def run_market_summary(nifty, vix):
    """Analyze key market metrics and regime."""
    high = fifty_two_week_high(nifty)
    low = fifty_two_week_low(nifty)
    volatility = annualized_volatility(nifty)

    dma20 = moving_averages(nifty, 20)
    dma50 = moving_averages(nifty, 50)
    dma200 = moving_averages(nifty, 200)

    print(f"52 Week High : {high:.2f}")
    print(f"52 Week Low : {low:.2f}")
    print(f"Annualized Volatility : {volatility:.2f}%")
    print(f"20 DMA : {dma20:.2f}")
    print(f"50 DMA : {dma50:.2f}")
    print(f"200 DMA : {dma200:.2f}")

    current_vix = latest_close(vix)
    fear_level = vix_regime(current_vix)

    current_price = nifty["Close"].iloc[-1].item()
    regime = market_regime(current_price, dma200)

    print("\nMARKET SUMMARY")
    print("-" * 30)
    print(f"Nifty Price : {current_price:.2f}")
    print(f"India VIX : {current_vix:.2f}")
    print(f"Fear Level : {fear_level}")
    print(f"Market Regime : {regime}")

    return current_price, current_vix, dma200


def run_breadth_analysis():
    """Analyze market breadth - percentage of stocks above 50-day MA."""
    above_50dma, total = breadth_analysis()
    breadth_score = above_50dma / total
    strength = breadth_strength(breadth_score)

    print("\nMARKET BREADTH")
    print("-" * 30)
    print(f"Stocks Above 50 DMA : {above_50dma}/{total}")
    print(f"Breadth Strength : {strength}")

    return breadth_score


def run_correlation_analysis(nifty, vix):
    """Analyze NIFTY-VIX correlation and regimes."""
    nifty_returns = daily_returns(nifty)
    vix_returns = daily_returns(vix)
    corr = correlation(nifty_returns, vix_returns)

    rolling_corr = rolling_correlation(nifty_returns, vix_returns)
    latest_rolling_corr = rolling_corr.iloc[-1]

    print("\nNIFTY <-> VIX CORRELATION")
    print("-" * 30)
    print(f"Correlation : {corr:.2f}")
    print(f"Latest Rolling Corr : {latest_rolling_corr:.2f}")

    regime = rolling_regime(latest_rolling_corr)
    print(f"Correlation Regime : {regime}")

    return rolling_corr


def run_visualizations(nifty, vix):
    """Generate market visualizations."""
    nifty["20DMA"] = nifty["Close"].rolling(20).mean()
    nifty["50DMA"] = nifty["Close"].rolling(50).mean()
    nifty["200DMA"] = nifty["Close"].rolling(200).mean()

    plot_nifty_trend(nifty)
    plot_vix(vix)


def run_signal_engine(current_price, dma200, current_vix, breadth_score):
    """Generate trading signal based on market conditions."""
    signal = trading_signal(current_price, dma200, current_vix, breadth_score)

    print("\nTRADING SIGNAL")
    print("-" * 30)
    print(f"Signal : {signal}")

    return signal


def run_backtest_engine(nifty):
    """Execute backtest on historical data."""
    portfolio = run_backtest(nifty)

    print("\nBACKTEST RESULTS")
    print("-" * 30)
    print(portfolio.stats())

    return portfolio


def run_optimizer(nifty):
    """Optimize strategy parameters."""
    results = optimize_strategy(nifty)

    print("\nSTRATEGY OPTIMIZATION")
    print("-" * 30)
    for result in results:
        print(
            f"MA: {result['MA']} | "
            f"Return: {result['Return']:.2f} | "
            f"Sharpe: {result['Sharpe']:.2f} | "
            f"Drawdown: {result['Drawdown']:.2f}"
        )

    return results


def run_walkforward(nifty):
    """Execute walk-forward validation."""
    train_pf, test_pf = walk_forward_test(nifty)

    print("\nWALK FORWARD TEST")
    print("-" * 30)
    print(f"Train Return : {train_pf.total_return().iloc[0]:.2f}")
    print(f"Test Return : {test_pf.total_return().iloc[0]:.2f}")

    return train_pf, test_pf


def run_research_suite(nifty, vix):
    """Execute all research studies."""
    print("\n" + "=" * 60)
    print("RESEARCH STUDIES")
    print("=" * 60)

    # VIX Study
    print("\nVIX REGIME STUDY")
    print("-" * 30)
    vix_df = vix_prepare_dataset(nifty, vix)
    vix_results = vix_analyse_regime(vix_df)
    print(vix_results)
    print("\nVIX STATISTICS")
    print(vix_df["VIX"].describe())
    print(vix_df["Regime"].value_counts())
    print(vix_df[["VIX", "Regime"]].head())

    # Trend Study
    print("\n\nTREND PERSISTENCE STUDY")
    print("-" * 30)
    trend_df = prepare_trend_dataset(nifty)
    trend_results = analyze_trend(trend_df)
    print(trend_results)

    # Drawdown Study
    print("\n\nDRAWDOWN RECOVERY STUDY")
    print("-" * 30)
    drawdown_df = prepare_drawdown_dataset(nifty)
    drawdown_results = analyse_drawdown(drawdown_df)
    print(drawdown_results)

    # Drawdown V2 Study
    print("\n\nDRAWDOWN DISTRIBUTION ANALYSIS")
    print("-" * 30)
    v2_results = drawdown_distribution(drawdown_df)
    print(v2_results)


# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

def main():
    """Main orchestrator - executes all analysis pipelines."""
    print("=" * 60)
    print("NIFTY 50 MARKET ANALYSIS")
    print("=" * 60)

    # Initialize market data
    nifty, vix = initialize_market()

    # Run analysis pipelines
    current_price, current_vix, dma200 = run_market_summary(nifty, vix)
    breadth_score = run_breadth_analysis()
    run_correlation_analysis(nifty, vix)
    run_visualizations(nifty, vix)
    run_signal_engine(current_price, dma200, current_vix, breadth_score)
    run_backtest_engine(nifty)
    run_optimizer(nifty)
    run_walkforward(nifty)
    run_research_suite(nifty, vix)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()

