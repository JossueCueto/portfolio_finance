import streamlit as st

# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

# Sección de perfil o resumen
st.sidebar.image('foto.jpg', caption='Jossue Cueto')
st.sidebar.write("Breve resumen sobre ti o tu experiencia")
st.sidebar.write("Otra información relevante")
st.sidebar.write("Contacto: tu_email@example.com")

# Descargar el resumen
st.sidebar.download_button('Descargar Resumen', 'path_to_resume.pdf', 'Tu Resumen.pdf')

# Sección principal de la aplicación
st.header('Snapshot de la Carrera')
st.subheader('Mi Introducción a Data Science')
st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')

# Puedes agregar más secciones aquí
# ...

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py





        

        
        
    
    
