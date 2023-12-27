def generate_html():
    # Contenedor externo con display flex y una consulta de medios para responsividad
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
            <img src='Foto.jpg' alt='Foto de Jossue Cueto' /> <!-- Asegúrate de que 'foto.jpg' sea accesible en la ubicación especificada -->
        </div>
        <div class='flex-item' style='text-align: center;'>
            <p>Jossue Cueto<br>Bachiller en Ciencias Administrativas</p>
        </div>
    </div>
    """
    return outer_container



