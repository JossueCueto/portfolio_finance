import datetime as dt
import yfinance as yf

def risk_free_function(start=None, end=None):
    if start is None:
        start = dt.date.today() - dt.timedelta(days=30)
    if end is None:
        end = dt.date.today()

    try:
        risk_free_data = yf.download('^TNX', start=start, end=end)['Adj Close']
        if risk_free_data.empty:
            raise ValueError("No se obtuvieron datos para ^TNX")
        risk_free_rate = float(risk_free_data.iloc[-1]) / 100
        return risk_free_rate
    except Exception as e:
        print(f"Error al obtener la tasa libre de riesgo: {e}")
        return 0.04  # Valor por defecto en caso de error
