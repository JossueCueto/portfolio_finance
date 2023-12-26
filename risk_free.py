import datetime as dt
import pandas_datareader.data as pdr

def risk_free_function(max_intentos):
    iteracion = 0
    max_intentos = 7  # Número máximo de días en el pasado que queremos buscar
    last_valid_risk_free_rate = None
    
    while last_valid_risk_free_rate is None and iteracion < max_intentos:
        try:
            start_risk_free = dt.date.today() - dt.timedelta(days=iteracion)
            end_risk_free = dt.date.today()
            risk_free_data = pdr.get_data_yahoo('^TNX', start_risk_free, end_risk_free)['Adj Close']
            risk_free_data = risk_free_data.dropna()
            
            if not risk_free_data.empty:
                last_valid_risk_free_rate = risk_free_data.iloc[-1]
                break  # Salir del bucle si encontramos un valor válido
        except Exception as e:
            print(f"No se pudo obtener el dato para la fecha {start_risk_free}: {e}")
        finally:
            iteracion += 1  # Aseguramos que la iteración se incremente en cada ciclo
    
    # Imprimir el último valor válido encontrado
    if last_valid_risk_free_rate is not None:
        last_valid_risk_free_rate=last_valid_risk_free_rate
    else:
        last_valid_risk_free_rate="No se pudo encontrar un valor válido en los últimos intentos."
