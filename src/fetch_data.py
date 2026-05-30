import yfinance as yf

nifty = yf.download("^NSEI", period = '1y')

print(nifty.tail())

latest_price  = nifty["Close"].iloc[-1]

daily_return = (nifty["Close"].pct_change().iloc[-1]*100)

print('latest price :' , latest_price)
print("daily return : " , daily_return)