import datetime as dt
import pandas_datareader.data as pdr

def risk_free_function(start=dt.date.today() - dt.timedelta(days=30),end=dt.date.today()):
    risk_free_data=pdr.get_data_yahoo('^TNX',start,end)['Adj Close']
    risk_free_rate = float(risk_free_data.iloc[-1])
    return print(risk_free_rate)

risk_free_function()
    if last_valid_risk_free_rate is not None:
        last_valid_risk_free_rate=last_valid_risk_free_rate
    else:
        last_valid_risk_free_rate="No se pudo encontrar un valor válido en los últimos intentos."
    return last_valid_risk_free_rate/100
