import streamlit as st

# Encabezado de la aplicación
st.title('Mi Aplicación de Data Science')

# Creación de columnas para la imagen y la información del perfil
col1, col2 = st.columns([1, 4])  # La proporción entre la imagen y el texto es 1:4

# En la columna 1: Agregar la imagen
with col1:
    st.image('foto.jpg', width=150)  # Ajusta el ancho de la imagen como prefieras

# En la columna 2: Agregar la información del perfil
with col2:
    st.subheader('Mehul Gupta')
    st.markdown('1,849 Puntos de Reputación')
    st.markdown('👍 3   💬 17   👀 34')  # Emojis para likes, comentarios y vistas

# Menú desplegable en la barra lateral
menu = st.sidebar.selectbox('Menu', ['Sobre mi', 'Trabajos'])

# Muestra la información basada en la selección del menú
if menu == 'Sobre mi':
    st.sidebar.write("Información sobre mí")
elif menu == 'Trabajos':
    st.sidebar.write("Información sobre mis trabajos anteriores o proyectos")

# Botón para descargar el resumen en la barra lateral
st.sidebar.download_button('Descargar Resumen', 'path_to_resume.pdf', 'Tu Resumen.pdf')

# Sección principal de la aplicación (puedes continuar desde aquí)
# ...

# Para ejecutar la aplicación, guarda el código en un archivo .py y ejecútalo con el comando:
# streamlit run tu_archivo.py

# Asegúrate de actualizar 'path_to_image.jpg' y 'path_to_resume.pdf' con las rutas reales a tus archivos.



        

        
        
    
    
