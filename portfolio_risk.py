import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "GOOGL"] 

data = yf.download(stocks, start="2020-01-01", end="2024-12-31")["Close"]

print(data.head())

returns = data.pct_change().dropna()

weights = [1/len(stocks)] * len(stocks)  
portfolio_returns = (returns @ weights)


avg_return = portfolio_returns.mean()
volatility = portfolio_returns.std()

print("Average Daily Return:", round(avg_return, 5))
print("Volatility (Std Dev):", round(volatility, 5))

# ~0.01% daily risk-free rate (standard norm)
risk_free_rate = 0.0001
sharpe_ratio = (avg_return - risk_free_rate) / volatility

print("Sharpe Ratio:", round(sharpe_ratio, 2))
