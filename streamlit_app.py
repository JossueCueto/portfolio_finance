import streamlit as st
from portfolio_simulation import run_simulation
from html_module import generate_html
from perfil_profesional import run_perfil_profesional

#Guardar contenido HTML
html_content = generate_html()

import streamlit as st

with st.sidebar:
    st.markdown(html_content, unsafe_allow_html=True)
    st.write(" ")
    # Puedes usar st.markdown para un control más fino del formato de texto, si es necesario
    st.markdown('Bachiller en Ciencias Administrativas con dominio intermedio de inglés, habilidades analíticas y comunicativas, enfocado en el mercado de capitales y gestión de portafolios.')
    st.write("Wish to connect?")
    st.write("jossue.cueto@gmail.com")  # Asegúrate de reemplazar esto con tu información real
    st.write("www.linkedin.com/in/jossue-cueto/")  # Asegúrate de reemplazar esto con tu información real
    st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf')

# Menú desplegable en la barra lateral
menu = st.sidebar.selectbox('Menu', ['Sobre mi', 'Trabajos'])

# Contenido principal de la aplicación que cambia basado en la selección del menú
if menu == 'Sobre mi':
    # Encabezado de la aplicación
    st.title('Perfil Profesional')
    # Contenido de 'Sobre mi'
    run_perfil_profesional()
elif menu == 'Trabajos':
    st.title('Optimización de portafolio')
    run_simulation()

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py

# Asegúrate de actualizar 'foto.jpg' y 'path_to_resume.pdf' con las rutas reales a tus archivos.


