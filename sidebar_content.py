# sidebar_content.py
import streamlit as st

def load_css():
    sidebar_css = """
    <style>
    .image-container {
        margin-right: 20px;  /* Aumenta el espacio entre la imagen y el texto */
    }
    .text-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
    """
    st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)

def display_sidebar_content():
    with st.sidebar:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image('foto.jpg', width=80)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write('Jossue Cueto')
        st.write('Bachiller en Ciencias Administrativas, interesado en el mercado de capitales')
        st.markdown('</div>', unsafe_allow_html=True)
