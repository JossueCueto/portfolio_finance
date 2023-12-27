import base64

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_html():
    image_base64 = get_image_base64('Foto.jpg')
    # Contenedor externo con display flex y una consulta de medios para responsividad
    outer_container = f"""
    <style>
        .flex-container {{
            display: flex;
            justify-content: space-around;
            align-items: center;
        }}
        @media (max-width: 720px) {{
            .flex-container {{
                flex-direction: column;
            }}
        }}
        .flex-item img {{
            max-width: 100%;
            height: auto;
            border-radius: 50%;  /* Opcional: hace la imagen circular */
        }}
    </style>
    <div class='flex-container'>
        <div class='flex-item' style='text-align: center;'>
            <img src="data:image/jpeg;base64,{image_base64}" alt='Foto de Jossue Cueto' />
        </div>
        <div class='flex-item' style='text-align: center;'>
            <p>Jossue Cueto<br>Bachiller en Ciencias Administrativas</p>
        </div>
    </div>
    """
    return outer_container

# En el script principal de Streamlit
html_content = generate_html()
st.markdown(html_content, unsafe_allow_html=True)


