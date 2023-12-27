# sidebar_content.py
import streamlit as st

def load_css():
    sidebar_css = """
    <style>
    .sidebar .sidebar-content {
        padding-top: 1rem; /* Espacio adicional en la parte superior */
    }
    .image-text-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding-right: 1rem; /* Espacio al final del contenedor para asegurar que el texto no toque los bordes */
    }
    .image-container {
        padding-right: 1rem; /* Espacio entre la imagen y el texto */
    }
    .text-container {
        flex-grow: 1; /* Permite que el contenedor de texto crezca si hay espacio disponible */
    }
    @media (max-width: 768px) {
        .image-text-container {
            flex-direction: column; /* Cambia a una disposición en columna en pantallas más pequeñas */
        }
        .image-container {
            padding-right: 0; /* Elimina el espaciado a la derecha en la disposición de columna */
        }
    }
    </style>
    """
    st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)

def display_sidebar_content():
    with st.sidebar:
        st.markdown('<div class="image-text-container">', unsafe_allow_html=True)
        
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image('foto.jpg', width=80)  # Ajusta el tamaño de la imagen como sea necesario
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write('Jossue Cueto')
        st.write('Bachiller en Ciencias Administrativas, interesado en el mercado de capitales')
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Cierra el contenedor principal

# sidebar_content.py
import streamlit as st

def load_css():
    sidebar_css = """
    <style>
    .sidebar .sidebar-content {
        padding-top: 1rem; /* Espacio adicional en la parte superior */
    }
    .image-text-container {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .text-container {
        margin-left: 1em; /* Espacio entre la imagen y el texto */
        /* Asegúrate de que el texto no se pegue al borde derecho en pantallas pequeñas */
        padding-right: 1em;
    }
    @media (max-width: 768px) {
        .image-text-container {
            flex-direction: column; /* Cambia a disposición en columna para pantallas pequeñas */
            padding-bottom: 1em;
        }
        .text-container {
            margin-left: 0; /* Elimina el margen izquierdo en disposición de columna */
        }
    }
    </style>
    """
    st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)

def display_sidebar_content():
    with st.sidebar:
        st.markdown('<div class="image-text-container">', unsafe_allow_html=True)
        
        st.image('foto.jpg', width=80)  # Ajusta el tamaño de la imagen como sea necesario
        
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write('Jossue Cueto')
        st.write('Bachiller en Ciencias Administrativas, interesado en el mercado de capitales')
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Cierra el contenedor principal
