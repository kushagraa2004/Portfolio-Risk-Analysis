import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "GOOGL"] 

data = yf.download(stocks, start="2020-01-01", end="2024-12-31")["Close"]

print(data.head())