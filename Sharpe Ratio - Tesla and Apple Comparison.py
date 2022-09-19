#!/usr/bin/env python
# coding: utf-8

# In[11]:


# import libraries.
import yfinance as yf
import numpy as np

# get the data.
data = yf.download(["TSLA", "AAPL"], start="2020-01-01", end="2022-07-31") # Tesla and General Electric.
closes = data['Adj Close']
tsla_returns = closes.TSLA.pct_change().dropna()
aapl_returns = closes.AAPL.pct_change().dropna()

# compute the sharpe ratio.
def sharpe_ratio(returns, adjustment_factor = 0.0):
    returns_risk_adj = returns - adjustment_factor
    return (returns_risk_adj.mean() / returns_risk_adj.std()) * np.sqrt(252)

# display investment
sharpe_ratio(tsla_returns)
sharpe_ratio(aapl_returns)
tsla_returns.rolling(30).apply(sharpe_ratio).plot()
aapl_returns.rolling(30).apply(sharpe_ratio).plot()


# In[ ]:




