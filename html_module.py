def generate_html():
    # Contenedor externo con display flex y una consulta de medios para responsividad
    outer_container = """
    <style>
        .flex-container {
            display: flex;
            justify-content: space-around;
        }
        @media (max-width: 720px) {
            .flex-container {
                flex-direction: column;
            }
        }
    </style>
    <div class='flex-container'>
        <div style='text-align: center;'>
            <h1>Bienvenido a Mi Aplicación de Data Science</h1>
        </div>
        <div style='text-align: center;'>
            <h2>Otro Encabezado</h2>
        </div>
    </div>
    """
    return outer_container

