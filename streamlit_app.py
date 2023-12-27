import streamlit as st
from portfolio_simulation import run_simulation
from sidebar_content import load_css, display_sidebar_content

# Aplicar el CSS personalizado para la barra lateral
load_css()

# Mostrar el contenido de la barra lateral
display_sidebar_content()

# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

# Menú desplegable en la barra lateral
menu = st.sidebar.selectbox('Menu', ['Sobre mi', 'Trabajos'])

# Contenido principal de la aplicación que cambia basado en la selección del menú
if menu == 'Sobre mi':
    # Contenido de 'Sobre mi'
    st.header('Snapshot de la Carrera')
    st.subheader('Mi Introducción a Data Science')
    st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
    # Puedes agregar más secciones aquí relacionadas con 'Sobre mi'
elif menu == 'Trabajos':
    run_simulation()


