import streamlit as st
from portfolio_simulation import run_portfolio_simulation
from html_module import generate_html
from perfil_profesional import run_perfil_profesional
import requests
from io import BytesIO

# Guardar contenido HTML
html_content = generate_html()

# Definir la variable 'menu' antes de usarla
menu = st.sidebar.selectbox('',['Perfil Profesional', 'Optmización de Portafolio'])
st.write(" ")

with st.sidebar:
    st.markdown(html_content, unsafe_allow_html=True)
    st.write(" ")
    if menu != 'Perfil Profesional':
        st.markdown('Bachiller en Ciencias Administrativas con dominio intermedio de Inglés, habilidades analíticas y comunicativas, enfocado en el área financiera.')
    st.write("Contactémonos")
    st.write("jossue.cueto@gmail.com")  # Asegúrate de reemplazar esto con tu información real
    st.write("www.linkedin.com/in/jossue-cueto/")  # Asegúrate de reemplazar esto con tu información real
    
    response_cv = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/CV_Jossue.pdf')
    pdf_cv = BytesIO(response_cv.content)
    st.download_button('Descargar CV', pdf_cv, 'Jossue_CV.pdf','application/pdf')

# Contenido principal de la aplicación que cambia basado en la selección del menú
if menu == 'Perfil Profesional':
    st.title('Perfil Profesional')
    run_perfil_profesional()
elif menu == 'Optmización de Portafolio':
    st.title('Optimización de Portafolio')
    run_portfolio_simulation()
