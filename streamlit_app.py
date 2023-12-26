import streamlit as st

# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

# Ajusta el tamaño de la imagen y cárgala en la barra lateral
st.sidebar.image('foto.jpg', caption='Tu Nombre', width=150)

# Menú desplegable en la barra lateral
menu = st.sidebar.selectbox('Menu', ['Sobre mi', 'Trabajos'])

# Muestra la información basada en la selección del menú
if menu == 'Sobre mi':
    st.sidebar.write("Información sobre mí")
elif menu == 'Trabajos':
    st.sidebar.write("Información sobre mis trabajos anteriores o proyectos")

# Botón para descargar el resumen
st.sidebar.download_button('Descargar Resumen', 'path_to_resume.pdf', 'Tu Resumen.pdf')

# Sección principal de la aplicación
st.header('Snapshot de la Carrera')
st.subheader('Mi Introducción a Data Science')
st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')

# Puedes agregar más secciones aquí
# ...

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py





        

        
        
    
    
