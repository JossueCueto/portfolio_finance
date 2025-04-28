import datetime as dt
import pandas_datareader.data as pdr
import yfinance as yf

def risk_free_function(start=dt.date.today() - dt.timedelta(days=30),end=dt.date.today()):
    risk_free_data=pdr.get_data_yahoo('^TNX',start,end)['Adj Close']
    risk_free_rate = float(risk_free_data.iloc[-1])
    risk_free_rate=risk_free_rate/100
    return risk_free_rate
