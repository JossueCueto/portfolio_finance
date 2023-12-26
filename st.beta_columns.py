import streamlit as st

# Título de tu aplicación o sección
st.title('Perfil del Usuario')

# Creación de dos columnas
col1, col2 = st.beta_columns([1, 4])  # La proporción entre la imagen y el texto es 1:4

# En la columna 1: Agregar la imagen
col1.image('foto.jpg', use_column_width=True)

# En la columna 2: Agregar la información
col2.subheader('Mehul Gupta')
col2.write('1,849 Puntos de Reputación')
col2.write('👍 3   💬 17   👀 34')  # Emojis para likes, comentarios y vistas

# Recuerda actualizar 'path_to_image.jpg' con la ruta real a tu imagen.
