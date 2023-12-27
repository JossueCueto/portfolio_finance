import streamlit as st
from portfolio_simulation import run_simulation
from html_module import generate_html
from perfil_profesional import run_perfil_profesional

# Guardar contenido HTML
html_content = generate_html()

with st.sidebar:
    st.markdown(html_content, unsafe_allow_html=True)
    st.write(" ")
    st.write("Wish to connect?")
    st.write("jossue.cueto@gmail.com")  # Asegúrate de reemplazar esto con tu información real
    st.write("www.linkedin.com/in/jossue-cueto/")  # Asegúrate de reemplazar esto con tu información real
    st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf')

    # Menú desplegable en la barra lateral
    menu = st.sidebar.selectbox('Menu', ['Sobre mi', 'Trabajos'])

# Condición para mostrar el texto adicional en la barra lateral, antes del menú
if menu != 'Sobre mi':
    with st.sidebar:
        st.markdown('Bachiller en Ciencias Administrativas con dominio intermedio de inglés, habilidades analíticas y comunicativas, enfocado en el mercado de capitales y gestión de portafolios.')

# Contenido principal de la aplicación que cambia basado en la selección del menú
if menu == 'Sobre mi':
    st.title('Perfil Profesional')
    run_perfil_profesional()
elif menu == 'Trabajos':
    st.title('Optimización de portafolio')
    run_simulation()


