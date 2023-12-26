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

    max_sharpe_idx = np.argmax(port_sharpe)
    max_sharpe_std = port_std[max_sharpe_idx]
    max_sharpe_rets = port_rets[max_sharpe_idx]

    plt.scatter(max_sharpe_std, max_sharpe_rets, c='red', s=50, marker='*')
    plt.title('Portfolio Optimization with the Sharpe Ratio')
    
    # Agregar líneas de utilidad
    valores_utilidad = np.linspace(0, max_sharpe, 50)
    valores_x = np.linspace(min(port_std), max(port_std), 100)
    for utilidad in valores_utilidad:
        plt.plot(valores_x, utilidad * valores_x, 'k-', linewidth=0.5, alpha=0.5)

    plt.xlim(min(port_std), max(port_std))
    plt.ylim(min(port_rets), max(port_rets))

    st.pyplot(plt)

def run_simulation():
    # PARTE 1: EXTRACCIÓN DE DATOS
    yf.pdr_override()

    st.title('Simulador de Portafolio de Inversiones')

    number_assets = st.number_input('Cuántos valores analizaremos:', min_value=1, value=2, step=1)
    start = st.text_input('Ingrese la fecha de inicio (YYYY-MM-DD):', '2020-01-01')
    end = st.text_input('Ingrese la fecha de cierre (YYYY-MM-DD):', '2021-01-01')

    daily_prices = pd.DataFrame()
    daily_returns = pd.DataFrame()

    if st.button('Obtener datos y realizar simulación'):
        with st.spinner('Obteniendo datos...'):
            for i in range(number_assets):
                asset_input = st.text_input(f'Ingrese el ticker del valor n°{i+1} a usar:', key=f'asset_{i}')
                if asset_input:
                    asset_data = pdr.get_data_yahoo(asset_input, start, end)
                    daily_prices[asset_input] = asset_data['Adj Close']
                    daily_returns[asset_input] = np.log(daily_prices[asset_input] / daily_prices[asset_input].shift(1))

            daily_returns.dropna(inplace=True)

            if not daily_returns.empty:
                perform_simulation(daily_returns, number_assets)
