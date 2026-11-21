def vix_regime(vix):
    if vix < 15:
        return "LOW FEAR"
    elif vix < 20:
        return "NORMAL"
    elif vix < 25:
        return "HIGH FEAR"
    return "PANIC"
