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
        }}
    </style>
    <div class='flex-container'>
        <div class='flex-item' style='text-align: center;'>
            <img src="{image_url}" alt='Foto de Jossue Cueto' />
        </div>
        <div class='flex-item' style='text-align: center;'>
            <p><strong>Jossue Enrique<br>Cuento Ninaja</strong></p>
        </div>
    </div>
    """
    return outer_container
