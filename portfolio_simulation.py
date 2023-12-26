import streamlit as st
import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import yfinance as yf

# PARTE 2: SIMULACIÓN DE PESOS DE PORTAFOLIO
def perform_simulation(daily_returns, number_assets):
    np.random.seed(10)
    npor = int(1e4)
    n_asset = number_assets
    ws = np.zeros((npor, n_asset))
    port_rets = np.zeros(npor)
    port_std = np.zeros(npor)
    port_sharpe = np.zeros(npor)
    Annual_units = 252

    for portafolio in range(npor):
        w = np.array(np.random.random(n_asset))
        w /= np.sum(w)
        ws[portafolio, :] = w
        port_rets[portafolio] = np.sum(daily_returns.mean() * w * Annual_units)
        port_std[portafolio] = np.sqrt(np.dot(w.T, np.dot(daily_returns.cov() * Annual_units, w)))
        port_sharpe[portafolio] = port_rets[portafolio] / port_std[portafolio]

    plt.scatter(port_std, port_rets, c=port_sharpe, cmap='viridis', s=10)
    plt.xlabel('Risk')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')

    max_sharpe=port_sharpe.max()
    max_sharpe_location=int(port_sharpe.argmax())
    max_sharpe_rets=port_rets[max_sharpe_location]
    max_sharpe_std=port_std[max_sharpe_location]

    plt.scatter(max_sharpe_std, max_sharpe_rets, c='red', s=50, marker='*')
    plt.title('Portfolio Optimization with the Sharpe Ratio')
    
    # Agregar líneas de utilidad
    valores_utilidad=np.linspace(0, 100,50)
    valores_utilidad=np.append(valores_utilidad,max_sharpe)
    valores_x=np.linspace(0, 100,25)
    for utilidad in valores_utilidad:
        plt.plot(valores_x, utilidad * valores_x, 'k-', linewidth=0.5, alpha=0.5)

    plt.xlim(min_risk-0.05, max_risk+0.05)
    plt.ylim(min_rets-0.05,max_rets+0.05)

    st.pyplot(plt)

def run_simulation():
    # PARTE 1: EXTRACCIÓN DE DATOS
    yf.pdr_override()

    st.title('Simulador de Portafolio de Inversiones')

    # Almacena el número de activos y las fechas en session_state para persistencia
    if 'number_assets' not in st.session_state:
        st.session_state['number_assets'] = 2
    if 'start' not in st.session_state:
        st.session_state['start'] = '2020-01-01'
    if 'end' not in st.session_state:
        st.session_state['end'] = '2021-01-01'

    number_assets = st.number_input('Cuántos valores analizaremos:', min_value=1, value=st.session_state['number_assets'], step=1)
    st.session_state['number_assets'] = number_assets
    start = st.text_input('Ingrese la fecha de inicio (YYYY-MM-DD):', st.session_state['start'])
    st.session_state['start'] = start
    end = st.text_input('Ingrese la fecha de cierre (YYYY-MM-DD):', st.session_state['end'])
    st.session_state['end'] = end

    # Inicializa los tickers en session_state
    for i in range(number_assets):
        if f'asset_{i}' not in st.session_state:
            st.session_state[f'asset_{i}'] = ''

    # Crea los campos de texto para los tickers
    tickers = []
    for i in range(number_assets):
        ticker = st.text_input(f'Ingrese el ticker del valor n°{i+1} a usar:', key=f'asset_{i}')
        tickers.append(ticker)

    # Botón para realizar la simulación
    if st.button('Obtener datos y realizar simulación'):
        with st.spinner('Obteniendo datos...'):
            daily_prices = pd.DataFrame()
            daily_returns = pd.DataFrame()

            for i, ticker in enumerate(tickers):
                if ticker:  # Asegurarse de que el ticker no esté vacío
                    asset_data = pdr.get_data_yahoo(ticker, start, end)
                    daily_prices[ticker] = asset_data['Adj Close']
                    daily_returns[ticker] = np.log(daily_prices[ticker] / daily_prices[ticker].shift(1))

            daily_returns.dropna(axis=0)

            if not daily_returns.empty:
                perform_simulation(daily_returns, number_assets)
            else:
                st.error('No se pudieron obtener datos para los tickers proporcionados.')
