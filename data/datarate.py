from fredapi import Fred
# import yfinance as yf
import pandas as pd
from utils.api import FRED_API_KEY
from utils.constants import date_start

# US YIELD CURVE
fred = Fred(api_key=FRED_API_KEY)

taux_1m = fred.get_series("DGS1MO", observation_start=date_start) 
taux_3m = fred.get_series("DGS3MO", observation_start=date_start)
taux_2y = fred.get_series("DGS2", observation_start=date_start)
taux_5y = fred.get_series("DGS5", observation_start=date_start)
taux_10y = fred.get_series("DGS10", observation_start=date_start)
taux_30y = fred.get_series("DGS30", observation_start=date_start)

df = pd.DataFrame({
    "1M": taux_1m,
    "3M": taux_3m,
    "2Y": taux_2y,
    "5Y": taux_5y,
    "10Y": taux_10y,
    "30Y": taux_30y
}).dropna()

print(df.head())

# Yahoo Finance : ETF obligations
# tickers = ['BND', 'TLT']
# etf_data = yf.download(tickers, start='2000-01-01', end='2025-01-01')
# print(etf_data.head())
# etf_adj = pd.DataFrame({ticker: etf_data['Adj Close'][ticker] for ticker in tickers})


