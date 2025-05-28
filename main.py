import streamlit as st
from landing import show_landing
from vistas.about_us import show_about
from vistas.noticias import show_news
from vistas.sensores import show_sensores
from vistas.visualizaciones import show_visualizacion
from vistas.login import login

st.set_page_config(page_title="IoT Dashboard", layout="wide")

# --- Estilos ---
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
.sidebar .sidebar-content .block-container {
    padding-top: 2rem;
}
.menu-button {
    display: block;
    width: 100%;
    background-color: #D50032;
    color: white;
    text-align: left;
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
}
.menu-button:hover {
    background-color: #A30026;
}
.blur-box {
    filter: blur(4px);
    pointer-events: none;
    user-select: none;
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)

# --- Estado de navegación ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- Menú lateral ---
with st.sidebar:
    st.image("images/upb.png", width=200)
    st.markdown("### Navegación")

    if st.button("🏠 Inicio", key="btn_inicio"):
        st.session_state.page = "landing"
    if st.button("📰 Noticias", key="btn_news"):
        st.session_state.page = "noticias"
    if st.button("👥 Sobre Nosotros", key="btn_about"):
        st.session_state.page = "about"

    # Secciones protegidas
    if st.session_state.authenticated:
        if st.button("🔧 Gestión de Sensores", key="btn_sensores"):
            st.session_state.page = "sensores"
        if st.button("📈 Visualización", key="btn_visual"):
            st.session_state.page = "visual"
    else:
        st.markdown('<div class="blur-box">🔧 Gestión de Sensores</div>', unsafe_allow_html=True)
        st.markdown('<div class="blur-box">📈 Visualización</div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.session_state.authenticated:
        st.success(f"Sesión iniciada como: {st.session_state['user']}")
        if st.button("🔒 Cerrar Sesión"):
            st.session_state.authenticated = False
            st.session_state.user = ""
            st.session_state.page = "landing"
    else:
        if st.button("🔑 Iniciar Sesión"):
            st.session_state.page = "login"
        
        st.markdown(
            "<small style='color: #666;'>Inicia sesión para explorar las secciones de <b>Gestión de Sensores</b> y <b>Visualización de Datos</b>.</small>",
            unsafe_allow_html=True
        )

# --- Contenido principal ---
if st.session_state.page == "landing":
    show_landing()
elif st.session_state.page == "noticias":
    show_news()
elif st.session_state.page == "about":
    show_about()
elif st.session_state.page == "sensores":
    show_sensores()
elif st.session_state.page == "visual":
    show_visualizacion()
elif st.session_state.page == "login":
    login()
else:
    show_landing()