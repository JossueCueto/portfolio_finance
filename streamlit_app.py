import streamlit as st
from portfolio_simulation import run_simulation
from html_module import generate_html

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
    st.subheader('Resumen Profesional')
    st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
    st.header('Educación y Formación Académica')
    st.subheader('NetValU')
    st.markdown("""
    - **Propuesta de Portafolio de inversión de renta fija**: Elaboración de un portafolio de inversión compuesto por 100% bonos corporativos en base a un análisis macroeconómico, sectorial y de ratios financieros de las empresas.
    - **Medición de Riesgos de Portafolio de Inversión**: Análisis del riesgo de mercado y su impacto en el portafolio, considerando variables macroeconómicas y sensibilidad a factores de riesgo.
    - **Evaluación del Riesgo Crediticio**: Evaluación de la calidad crediticia para la compra de un bono corporativo de la empresa H2Olmos usando métricas de riesgo de crédito.
    - **Budget de Flujo de Caja y P&L**: Estimación de los resultados financieros de la compañía Netflix en los últimos 2 trimestres del 2023.
    """)
    st.subheader('Objetivos Profesionales')
    st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
    st.subheader('Desarrollo Personal y Profesional')
    st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
    st.subheader('Experiencia adicional')
    st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
    # Puedes agregar más secciones aquí relacionadas con 'Sobre mi'
elif menu == 'Trabajos':
    st.title('Optimización de portafolio')
    run_simulation()

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py

# Asegúrate de actualizar 'foto.jpg' y 'path_to_resume.pdf' con las rutas reales a tus archivos.


