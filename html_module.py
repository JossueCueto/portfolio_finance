def generate_html():
    # Asegúrate de reemplazar la URL de abajo con la URL de tu imagen en bruto de GitHub
    image_url = 'https://github.com/your_username/your_repository/raw/main/Foto.jpg'
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
            <img src="{image_url}" alt='Foto de Jossue Cueto' />
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


