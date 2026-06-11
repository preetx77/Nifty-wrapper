def trading_signal(current_price, dma200, vix, breadth_score):
    if (
        current_price > dma200
        and vix < 15
        and breadth_score > 0.7
    ):
        return "BUY"
    elif (
        current_price < dma200
        and vix > 20
    ):
        return "SELL"

    else:
        return "HOLD"
