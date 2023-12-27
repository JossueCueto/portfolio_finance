import streamlit as st
import base64

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def generate_html(image_base64):
    outer_container = f"""
    <style>
        .flex-container {{
            display: flex;
            justify-content: space-around;
            align-items: center; /* Alinea verticalmente los elementos dentro del contenedor */
        }}
        @media (max-width: 720px) {{
            .flex-container {{
                flex-direction: column;
            }}
        }}
        .flex-item img {{
            max-width: 100%; /* Asegura que la imagen sea responsive */
            height: auto;
        }}
    </style>
    <div class='flex-container'>
        <div class='flex-item' style='text-align: center;'>
            <img src="data:image/jpeg;base64,{image_base64}" alt='Foto de Jossue Cueto' /> <!-- Imagen en base64 -->
        </div>
        <div class='flex-item' style='text-align: center;'>
            <p>Jossue Cueto<br>Bachiller en Ciencias Administrativas</p>
        </div>
    </div>
    """
    return outer_container

# Ruta a la imagen
image_path = 'Foto.jpg'
# Convertir la imagen a base64
image_base64 = get_image_base64(image_path)
# Generar el HTML con la imagen en base64
html_content = generate_html(image_base64)

# En tu aplicación Streamlit
st.markdown(html_content, unsafe_allow_html=True)


