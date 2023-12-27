import streamlit as st

def load_css():
    sidebar_css = """
    <style>
    .sidebar .sidebar-content {
        padding-top: 1rem;  /* Espacio adicional en la parte superior */
    }
    .image-text-container {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .image-container {
        margin-right: 1rem;  /* Espacio entre la imagen y el texto */
    }
    .text-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """
    st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)

def display_sidebar_content():
    with st.sidebar:
        # Contenedor para la imagen y el texto
        st.markdown('<div class="image-text-container">', unsafe_allow_html=True)
        
        # Contenedor para la imagen con espaciado personalizado
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image('foto.jpg', width=80)  # Ajusta el tamaño de la imagen como sea necesario
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Contenedor para el texto
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write('Jossue Cueto')
        st.write('Bachiller en Ciencias Administrativas, interesado en el mercado de capitales')
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Cierra el contenedor principal

        # Añade otros elementos como el correo electrónico y el enlace de LinkedIn
        st.write('Wish to connect?')
        st.write('jossue.cueto@gmail.com')
        st.markdown('[www.linkedin.com/in/jossue-cueto/](https://www.linkedin.com/in/jossue-cueto/)')
        st.button('Download Resume')
