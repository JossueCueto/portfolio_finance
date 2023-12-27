# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

with st.sidebar:
    # Añade un espaciador en la parte superior si es necesario
    st.empty()

    # Define las columnas con una proporción que prefieras
    col1, col2 = st.columns([1, 4])

    with col1:
        # Añade la imagen
        st.image('foto.jpg', width=80)  # Ajusta el tamaño de la imagen como sea necesario

    with col2:
        # Añade un espaciador horizontal antes del texto para incrementar el espacio
        st.write(" ")  # Incrementa el número de espacios si es necesario

        # Añade el texto
        st.write('Jossue Cueto')
        st.write('Bachiller en Ciencias Administrativas, interesado en el mercado de capitales')

    # Añade un espaciador en la parte inferior si es necesario
    st.empty()

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


