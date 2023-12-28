import streamlit as st
from portfolio_simulation import run_portfolio_simulation
from html_module import generate_html
from perfil_profesional import run_perfil_profesional

# Guardar contenido HTML
html_content = generate_html()

# Definir la variable 'menu' antes de usarla
menu = st.sidebar.selectbox('',['Sobre mi', 'Trabajos'])
st.write(" ")

with st.sidebar:
    st.markdown(html_content, unsafe_allow_html=True)
    st.write(" ")
    if menu != 'Perfil Profesional':
        st.markdown('Bachiller en Ciencias Administrativas con dominio intermedio de inglés, habilidades analíticas y comunicativas, enfocado en el mercado de capitales y gestión de portafolios.')
    st.write("Contactémonos")
    st.write("jossue.cueto@gmail.com")  # Asegúrate de reemplazar esto con tu información real
    st.write("www.linkedin.com/in/jossue-cueto/")  # Asegúrate de reemplazar esto con tu información real
    st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf')

# Contenido principal de la aplicación que cambia basado en la selección del menú
if menu == 'Perfil Profesional':
    st.title('Perfil Profesional')
    run_perfil_profesional()
elif menu == 'Trabajos':
    st.title('Optimización de portafolio')
    run_portfolio_simulation()
