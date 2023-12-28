import streamlit as st
import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
from risk_free import risk_free_function as rf

# PARTE 2: SIMULACIÓN DE PESOS DE PORTAFOLIO
def perform_simulation(daily_returns, number_assets,tickers,industry_data):
    np.random.seed(10)
    npor = int(3e4)
    n_asset = number_assets
    ws = np.zeros((npor, n_asset))
    port_rets = np.zeros(npor)
    port_std = np.zeros(npor)
    port_sharpe = np.zeros(npor)
    Annual_units = 252
    risk_free_rate=float(rf())
    #risk_free_rate=0.03
    
    for portafolio in range(npor):
        w = np.array(np.random.random(n_asset))
        w = w/np.sum(w)
        ws[portafolio, :] = w
        port_rets[portafolio] = np.sum(daily_returns.mean() * w * Annual_units)
        port_std[portafolio] = np.sqrt(np.dot(w.T, np.dot(daily_returns.cov() * Annual_units, w)))
        port_sharpe[portafolio] = (port_rets[portafolio]-risk_free_rate) / port_std[portafolio]

    plt.scatter(port_std, port_rets, c=port_sharpe, cmap='viridis', s=10)
    
    plt.xlabel('Risk')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')

    max_sharpe=port_sharpe.max()
    max_sharpe_location=int(port_sharpe.argmax())
    max_sharpe_rets=port_rets[max_sharpe_location]
    max_sharpe_std=port_std[max_sharpe_location]

    min_risk=port_std.min()
    max_risk=port_std.max()
    min_rets=port_rets.min()
    max_rets=port_rets.max()

    plt.scatter(max_sharpe_std, max_sharpe_rets, c='red', s=50)
    plt.title('Portfolio Optimization with the Sharpe Ratio')
    
    # Agregar líneas de utilidad
    valores_utilidad=np.linspace(0, 100,75)
    valores_utilidad=np.append(valores_utilidad,max_sharpe)
    valores_x=np.linspace(0, 100,25)
    for utilidad in valores_utilidad:
        plt.plot(valores_x, utilidad * valores_x, 'k-', linewidth=0.5, alpha=0.5)

    plt.xlim(min_risk-0.05, max_risk+0.05)
    plt.ylim(min_rets-0.05,max_rets+0.05)
    
    #PARTE 5: GENERAR TABLA DE CARTERA
    
    # Extrayendo los vectores
    vector1 = industry_data
    vector2 = ws[max_sharpe_location, :]
    vector3 = daily_returns.mean()*Annual_units
    vector4 = daily_returns.std()

    valor1=max_sharpe_std
    valor2=max_sharpe_rets
    
    # Creando el DataFrame
    df = pd.DataFrame({'Industria': vector1, 'Peso': vector2,'Rentabilidad Anual': vector3, 'Volatilidad Anual': vector4})
    port_df = pd.DataFrame({'Volatilidad': [valor1], 'Retorno':  [valor2]},index=['Portafolio'])
    
    #PARTE 6: EXHIBICIÓN DE RESULTADOS
    # Usar st.columns para crear dos columnas
    col1, col2 = st.columns(2)

    # En la primera columna, mostrar información textual y DataFrame
    with col1:
        
        # Mostrar el primer DataFrame
        st.subheader("Volatilidad y Retorno de la Cartera")
        st.dataframe(port_df)
        
        # Mostrar el segundo DataFrame
        st.subheader("Detalle de la Cartera")
        st.dataframe(df)
        
    # En la segunda columna, mostrar el gráfico
    with col2:
        # Para mostrar un gráfico matplotlib en Streamlit
        st.pyplot(plt)
        # Nota: no es necesario llamar a plt.show() cuando se usa st.pyplot()
        st.write(f'La tasa libre de riesgo es {risk_free_rate}')

def run_portfolio_simulation():
    # PARTE 1: EXTRACCIÓN DE DATOS
    yf.pdr_override()

    st.write('Maximice el rendimiento ajustado al riesgo de sus inversiones. Esta aplicación ofrece simulaciones Monte Carlo y análisis de cartera para ayudarle a encontrar la combinación ideal de activos. Con acceso a datos financieros de Yahoo Finance en tiempo real y visualizaciones claras de rendimiento y riesgo, permitiendo simplificar la toma de decisiones estratégicas en inversiones.')

    # Almacena el número de activos y las fechas en session_state para persistencia (valores por defecto)
    if 'number_assets' not in st.session_state:
        st.session_state['number_assets'] = 2
    if 'start' not in st.session_state:
        st.session_state['start'] = dt.date.today() - dt.timedelta(days=365)
    if 'end' not in st.session_state:
        st.session_state['end'] = dt.date.today()
        
    col1, col2,col3= st.columns(3)
    with col1:
        # Almacena el número de activos y las fechas que se escriban
        number_assets = st.number_input('Cuántos valores analizaremos:', min_value=1, value=st.session_state['number_assets'], step=1)
        st.write('')
        st.session_state['number_assets'] = number_assets
    with col2:
        start = st.text_input('Ingrese la fecha de inicio (YYYY-MM-DD):', st.session_state['start'])
        st.session_state['start'] = start
    with col3:
        end = st.text_input('Ingrese la fecha de cierre (YYYY-MM-DD):', st.session_state['end'])
        st.session_state['end'] = end

    # Inicializa los tickers en session_state
    # st.session_state es una herramienta para mantener información entre diferentes ejecuciones del script.
    # actúa como un diccionario que Streamlit utiliza para recordar información a lo largo de la interacción del usuario con la aplicación web.
    for i in range(number_assets):
        if f'asset_{i}' not in st.session_state:
            st.session_state[f'asset_{i}'] = ''

    # Crea los campos de texto para los tickers
    tickers = []
    for i in range(number_assets):
        ticker = st.text_input(f'Ingrese el ticker del valor n°{i+1} a usar:', key=f'asset_{i}')
        #Se crea una lista tickers con los ticker ingresados en los campos de texto
        tickers.append(ticker)

    # Botón para realizar la simulación
    if st.button('Obtener datos y realizar simulación'):
        with st.spinner('Obteniendo datos...'):
            daily_prices = pd.DataFrame()
            daily_returns = pd.DataFrame()
            industry_data=[]
            
            for ticker in tickers:
                if ticker:  # Asegurarse de que el ticker no esté vacío
                    asset_data = pdr.get_data_yahoo(ticker, start, end)
                    daily_prices[ticker] = asset_data['Adj Close']
                    daily_returns[ticker] = np.log(daily_prices[ticker] / daily_prices[ticker].shift(1))
                    industry=yf.Ticker(ticker).info.get('industry', 'Industria no disponible')
                    industry_data=np.append(industry_data, industry)

            daily_returns.dropna(axis=0)

            if not daily_returns.empty:
                perform_simulation(daily_returns, number_assets,tickers,industry_data)
            else:
                st.error('No se pudieron obtener datos para los tickers proporcionados.')
