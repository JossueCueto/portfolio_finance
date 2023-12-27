import datetime as dt
import pandas_datareader.data as pdr

def risk_free_function(start=dt.date.today() - dt.timedelta(days=30), end=dt.date.today()):
    try:
        risk_free_data = pdr.get_data_yahoo('^TNX', start, end)['Adj Close']
        if not risk_free_data.empty:
            risk_free_rate = float(risk_free_data.iloc[-1]) / 100  # Convertir a tasa decimal
            return risk_free_rate
        else:
            return None  # No se encontraron datos
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return None

# Ejemplo de llamada a la función y imprimir el resultado
risk_free_rate = risk_free_function()
print(risk_free_rate if risk_free_rate is not None else "No se pudo obtener la tasa libre de riesgo.")
