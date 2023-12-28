def generate_html():
    #URL de la foto
    image_url = 'https://github.com/JossueCueto/portfolio_finance/blob/c0d65e5bbec6db2e83a061b9758d9ef39d642b72/img/Foto.jpg'
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
            border-radius: 50%; 
        }}
    </style>
    <div class='flex-container'>
        <div class='flex-item' style='text-align: center;'>
            <img src="{image_url}" alt='Foto de Jossue Cueto' />
        </div>
        <div class='flex-item' style='text-align: center;'>
            <p><strong>Jossue Enrique<br>Cueto Ninaja</strong><br>CEFA - BCRP | NetValU | UNJBG</p>
        </div>
    </div>
    """
    return outer_container
