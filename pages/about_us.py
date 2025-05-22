import streamlit as st
import io
from PIL import Image
import base64
import base64
from pathlib import Path
import time
import pandas as pd
import random
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Sobre Nosotros | Mi Equipo",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def img_to_bytes(img_path):
    try:
        img = Image.open(img_path)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        return ""

# CSS personalizado para animaciones y estilos
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background-color: #f8f9fa;
        padding: 0 !important;
    }
    
    h1, h2, h3 {
        color: #2c3e50;
    }
    
    .header-container {
        background: linear-gradient(135deg, #D50032 0%, #FF4081 100%);
        padding: 3rem 0;
        text-align: center;
        border-radius: 0 0 2rem 2rem;
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-in-out;
    }
    
    .team-header {
        color: white !important;
        margin-bottom: 1rem !important;
        font-weight: 700 !important;
        font-size: 3rem !important;
    }
    
    .team-subheader {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 300 !important;
        max-width: 700px;
        margin: 0 auto !important;
        font-size: 1.2rem !important;
    }
    
    .team-card {
        background-color: white;
        border-radius: 1rem;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: auto;
        display: flex;
        flex-direction: column;
        padding-bottom: 2rem;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    .member-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto;
        border: 3px solid #D50032;
        padding: 3px;
    }
    
    .member-name {
        color: #D50032;
        font-weight: 600;
        margin-top: 1rem !important;
        font-size: 1.4rem !important;
        text-align: center;
        padding-bottom: 1rem; /* Agrega un padding para que se muestre más grande hacia abajo */
    }
    
    .member-role {
        color: #D50032;
        font-weight: 500;
        margin-top: 0.3rem !important;
        text-align: center;
        font-size: 1rem !important;
    }
    
    .member-bio {
        margin-top: 1rem !important;
        font-size: 0.95rem !important;
        color: #4a5568;
        flex-grow: 1;
    }
    
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 0.75rem;
        margin-top: 1rem;
    }
    
    .social-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        background-color: #f1f5f9;
        border-radius: 50%;
        color: #D50032;
        font-size: 1rem;
        transition: all 0.2s ease;
    }
    
    .social-icon:hover {
        background-color: #D50032;
        color: white;
    }
    
    .cta-button {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(135deg,rgb(198, 17, 177) 0%, #FF4081 100%);
        color: white !important;
        border-radius: 50px;
        text-align: center;
        text-decoration: none;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .cta-button:hover {
        background: linear-gradient(135deg, #B71C1C 0%, #E91E63 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        color: white !important;
    }
    
    .cta-secondary {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background-color:rgb(151, 145, 145);
        color: white !important;
        border-radius: 50px;
        text-align: center;
        text-decoration: none;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .cta-secondary:hover {
        background-color: #5a6268;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        color: white !important;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .staggered-animation {
        opacity: 0;
        animation: slideIn 0.5s ease-out forwards;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        background-color: #FFFFFF;
        border-radius: 1rem;
    }
    
    /* Para dispositivos móviles */
    @media (max-width: 768px) {
        .team-header {
            font-size: 2rem !important;
        }
        
        .team-subheader {
            font-size: 1rem !important;
        }
    }
            

</style>
""", unsafe_allow_html=True)

# HTML para íconos de Font Awesome
fontawesome_html = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
"""
st.markdown(fontawesome_html, unsafe_allow_html=True)

# Contenedor del encabezado con animación
st.markdown("""
<div class="header-container">
    <h1 class="team-header">Nuestro Equipo</h1>
    <p class="team-subheader">Conoce a las personas talentosas y apasionadas detrás de nuestro proyecto de IOT. Cada uno aporta un conjunto único de habilidades para crear algo increíble.</p>
    <div style="margin-top: 2rem;">
        <a href="#" class="cta-button">Contacta con nosotros</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Función para la animación por pasos
def staggered_animation():
    for i in range(4):
        cols = st.columns(4)
        with cols[i]:
            st.markdown(f"""
            <div class="staggered-animation" style="animation-delay: {i * 0.2}s;">
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.1)




# Datos de los miembros del equipo (el mismo que tenías)
team_members = [
    {
        "name": "Sebastian Forero Duque",
        "bio": "Sebastian Forero es un estudiante de ingeniería de sistemas e informática, con habilidades Infraestructura de nube con aws, se unió al equipo con la visión de crear soluciones que impacten positivamente en la sociedad.",
        "image": "images/forero.png"
    },
    {
        "name": "Santiago Gallego Henao",
        "bio": "Un estudiante de ingeniería de sistemas e informática con fortalezas en arquitectura de software y desarrollo backend, Santiago garantiza que nuestras soluciones sean robustas, escalables y utilicen tecnologías innovadoras.",
        "image": "images/santiago.png"
    },
    {
        "name": "Maryangela Balcarcel Alarcon",
        "bio": "Con un ojo agudo para el diseño y la usabilidad, Maryangela tiene experiencia con el manejo de todo tipo de bases de datos y su enfoque centrado en el usuario garantiza que nuestros productos sean accesibles y fáciles de usar.",
        "image": "images/maryangela.png"
    },
    {
        "name": "Yeison Andres Muñoz Ceron",
        "bio": "Yeison combina habilidades de frontend y diseño para crear soluciones web completas. Su pasión por el código limpio y sus estudios de ingeniería en diseño y entretenimiento digital se refleja en cada proyecto que toca con mucha dedicación.",
        "image": "images/yeisson.png"
    }
]



# Código javascript para animación de aparición al hacer scroll
scroll_animation_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, {threshold: 0.1});
    
    document.querySelectorAll('.team-card').forEach(card => {
        observer.observe(card);
    });
});
</script>
"""

# Función para mostrar tarjetas de miembro con una pequeña animación secuencial
def display_team_members():
    cols = st.columns(4)

    for i, member in enumerate(team_members):
        img_src = img_to_bytes(member['image'])  # Ejecuta antes

        with cols[i]:
            social_html = ""
            for platform, url in member.get("social", {}).items():
                icon = {
                    "linkedin": "fab fa-linkedin-in",
                    "twitter": "fab fa-twitter",
                    "github": "fab fa-github",
                    "dribbble": "fab fa-dribbble",
                    "behance": "fab fa-behance",
                    "medium": "fab fa-medium-m"
                }.get(platform, "")

                if icon:
                    social_html += f"""
                        <a href="{url}" target="_blank" class="social-icon">
                            <i class="{icon}"></i>
                        </a>
                    """

            st.markdown(f"""
            <div class="team-card staggered-animation" style="animation-delay: {i * 0.2}s;">
                <img src="{img_src}" class="member-img" alt="{member['name']} ">
                <h3 class="member-name" style="color: #D50032" > {member['name']} </h3>
                <p class="member-role">{member.get('role', '')}</p>
                <p class="member-bio">{member['bio']}</p>
                <div class="social-icons">{social_html}</div>
            </div>
            """, unsafe_allow_html=True)



# Mostrar los miembros del equipo
display_team_members()

# Agregar alguna animación interactiva para las estadísticas del equipo
st.markdown("<h2 style='text-align: center; margin-top: 3rem; margin-bottom: 2rem;'>Nuestros Logros</h2>", unsafe_allow_html=True)

# Crear columnas para estadísticas con contador animado
stats_cols = st.columns(4)

with stats_cols[0]:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
        <h3 style="font-size: 2.5rem; font-weight: 700; color: #D50032;">End Devices</h3>
        <p style="color: #4a5568;">Completamos la configuración de múltiples end devices a través de platformio</p>
    </div>
    """, unsafe_allow_html=True)

with stats_cols[1]:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
        <h3 style="font-size: 2.5rem; font-weight: 700; color: #D50032;">ETL</h3>
        <p style="color: #4a5568;">Logramos hacer extracción, transformación y carga de datos, utilizando diversas técnicas de interpolación con python</p>
    </div>
    """, unsafe_allow_html=True)

with stats_cols[2]:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
        <h3 style="font-size: 2.5rem; font-weight: 700; color: #D50032;">Nube</h3>
        <p style="color: #4a5568;">Utilizamos la nube de aws para construir clientes y brokers para soluciones de IOT</p>
    </div>
    """, unsafe_allow_html=True)

with stats_cols[3]:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
        <h3 style="font-size: 2.5rem; font-weight: 700; color: #D50032;">Visualización</h3>
        <p style="color: #4a5568;">Realizamos visualicaciones orientadas al entendimiento del usuario con ayuda de Streamlit </p>
    </div>
    """, unsafe_allow_html=True)



# Pie de página con imagen INTEGRADA
st.markdown(f"""
<div class="footer">
    <img src="{img_to_bytes('images/upb.png')}" style="width: 300px; display: block; margin: 0 auto;">
</div>
""", unsafe_allow_html=True)

# Contador de visitantes simulado
st.sidebar.markdown("### Visitantes")
count = st.sidebar.empty()
current_count = random.randint(200, 300)
count.metric("Visitantes hoy", current_count)