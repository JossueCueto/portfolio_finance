def generate_html():
    # Asegúrate de reemplazar la URL de abajo con la URL de tu imagen en bruto de GitHub
    image_url = 'https://raw.githubusercontent.com/JossueCueto/portfolio_finance/main/Foto.jpg'
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
            max-width: 80px;
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
