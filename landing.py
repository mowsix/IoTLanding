import streamlit as st

# Configuración de la página principal
st.set_page_config(page_title="Landing UPB", layout="wide")

# Incluir el CSS personalizado
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

    body {
        font-family: 'Montserrat', sans-serif;
        color: #000000;
        background-color: #F5F5F5;
    }

    .header {
        padding: 1rem;
        background: linear-gradient(90deg, #D50032, #FF4081);
        color: white !important;
        border-radius: 5px;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo-title h2 {
        margin: 0;
    }

    .nav-link {
        color: white !important;
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem;
        border-radius: 4px;
        transition: background-color 0.3s;
        margin-right: 0.5rem;
    }
    .nav-link:hover {
        background-color: rgba(255,255,255,0.2) !important;
    }

    .hero {
        background-color: #F5F5F5;
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
    }

    .content-card {
        background-color: white;
        border-radius: 8px;
        padding: 1.5rem;
        border: 1px solid #eaeaea;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    .news-card {
        background-color: white;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #eaeaea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .news-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }

    .news-content {
        padding: 1rem;
    }

    .news-date {
        color: #000000;
        font-size: 0.8rem;
        margin-bottom: 0.5rem;
    }

    .footer {
        padding: 2rem 0;
        background-color: #F5F5F5;
        color: #D50032;
        text-align: center;
        margin-top: 3rem;
        border-top: 1px solid #eaeaea;
    }

    .section-title {
        color: #D50032;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }
</style>""", unsafe_allow_html=True)


# Encabezado
st.markdown("""
<div class="header">
  <div class="logo-title">
    <h2>Universidad Pontificia Bolivariana</h2>
  </div>
</div>
""", unsafe_allow_html=True)

# Menú de navegación
cols = st.columns([1, 1, 1, 1, 1])
with cols[0]:
    st.page_link("landing.py", label="🏠 Inicio", icon="🏠")
with cols[1]:
    st.page_link("pages/Login.py", label="Login", icon="🔐")
with cols[2]:
    st.page_link("pages/about_us.py", label="Acerca de", icon="ℹ️")
with cols[3]:
    st.page_link("pages/noticias.py", label="Noticias", icon="📰")
with cols[4]:
    if st.session_state.get("authenticated"):
        st.page_link("pages/sensores.py", label="Sensores", icon="📊")
    else:
        st.markdown(" ", unsafe_allow_html=True)

# Contenido principal
st.markdown("# Bienvenido al Proyecto de Sensores Ambientales de la UPB")
st.markdown("Este proyecto tiene como objetivo monitorear variables ambientales mediante sensores distribuidos en la sede de la Universidad.")

st.markdown("## ¿Qué encontrarás aquí?")
st.markdown("- Información general sobre el proyecto.")
st.markdown("- Visualizaciones de datos en tiempo real.")
st.markdown("- Registro de usuarios y autenticación.")

st.markdown("## Imágenes destacadas")
cols = st.columns(3)
for col in cols:
    with col:
        st.image("images/Sensores.png", use_container_width=True)

st.markdown("<div class='footer'>© 2025 Universidad Pontificia Bolivariana</div>", unsafe_allow_html=True)

