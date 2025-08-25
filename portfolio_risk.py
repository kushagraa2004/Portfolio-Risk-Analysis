import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

trading_days = 252

annual_return = avg_return * trading_days
annual_volatility = volatility * (trading_days ** 0.5)
annual_sharpe = annual_return / annual_volatility

print("Annual Return:", round(annual_return, 4))
print("Annual Volatility:", round(annual_volatility, 4))
print("Annual Sharpe Ratio:", round(annual_sharpe, 4))

portfolio_returns = returns.mean(axis=1)

# Historical VaR at 95% and 99%
var_95 = np.percentile(portfolio_returns, 5)   # 5th percentile (left tail)
var_99 = np.percentile(portfolio_returns, 1)   # 1st percentile

print("Value at Risk (95%):", round(var_95, 4))
print("Value at Risk (99%):", round(var_99, 4))

plt.figure(figsize=(10,6))
plt.hist(portfolio_returns, bins=50, color="skyblue", edgecolor="black", alpha=0.7)

# Mark VaR thresholds
plt.axvline(var_95, color="red", linestyle="dashed", linewidth=2, label=f"VaR 95%: {round(var_95,4)}")
plt.axvline(var_99, color="darkred", linestyle="dashed", linewidth=2, label=f"VaR 99%: {round(var_99,4)}")

plt.title("Portfolio Daily Returns Distribution with Value at Risk (VaR)")
plt.xlabel("Daily Returns")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("VaR_distribution.png")
plt.show()