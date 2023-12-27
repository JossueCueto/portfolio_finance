import streamlit as st
from portfolio_simulation import run_simulation

# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

with st.sidebar:
    # Utilizamos las proporciones deseadas para las columnas
    col1, col2 = st.columns([1, 4])

    with col1:
        # Añadimos la imagen con el tamaño que queramos
        st.image('foto.jpg', width=80)
    
    with col2:
        # Añadimos un estilo en línea al texto para agregar un margen a la izquierda
        st.markdown("""
        <style>
        .spacer {
            margin-left: 20px;  /* Ajusta este valor según sea necesario */
        }
        </style>
        <div class="spacer">
        <p>Jossue Cueto</p>
        <p>Bachiller en Ciencias Administrativas, interesado en el mercado de capitales</p>
        </div>
        """, unsafe_allow_html=True)

# Agrega más información debajo de las columnas anidadas en la barra lateral si es necesario
st.sidebar.write("Wish to connect?")
st.sidebar.write("jossue.cueto@gmail.com")  # Asegúrate de reemplazar esto con tu información real
st.sidebar.write("www.linkedin.com/in/jossue-cueto/")  # Asegúrate de reemplazar esto con tu información real
st.sidebar.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf')

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

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py

# Asegúrate de actualizar 'foto.jpg' y 'path_to_resume.pdf' con las rutas reales a tus archivos.

