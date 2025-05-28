import streamlit as st
import io
from PIL import Image
import base64
from pathlib import Path
import time
import pandas as pd
import random
import streamlit.components.v1 as components

def img_to_bytes(img_path):
    try:
        img = Image.open(img_path)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        return ""

def show_about():
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
            border: 3px solid #FFFFF;
            padding: 3px;
        }
        .member-name {
            color: #D50032;
            font-weight: 600;
            margin-top: 1rem !important;
            font-size: 1.4rem !important;
            text-align: center;
            padding-bottom: 1rem;
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
            color: white;
            flex-grow: 1;
        }
        .footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
            background-color: #FFFFFF;
            border-radius: 1rem;
        }
        .glassy-card {
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.05);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
            color: white;
        }
        
        .cta-button {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, rgb(198, 17, 177) 0%, #FF4081 100%);
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
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animate-fade-in {
            animation: fadeInUp 0.8s ease-out both;
        }

    </style>
    """, unsafe_allow_html=True)

    fontawesome_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """
    st.markdown(fontawesome_html, unsafe_allow_html=True)

    st.markdown("""
<div class="header-container">
    <h1 class="team-header">Nuestro Equipo</h1>
    <p class="team-subheader">Conoce a las personas talentosas y apasionadas detrás de nuestro proyecto de IOT. Cada uno aporta un conjunto único de habilidades para crear algo increíble.</p>
    <div style="margin-top: 2rem;">
        <a href="#" class="cta-button animate-fade-in">Contacta con nosotros</a>
    </div>
</div>
""", unsafe_allow_html=True)


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
            "image": "images/maryangela.jpeg"
        },
        {
            "name": "Yeison Andres Muñoz Ceron",
            "bio": "Yeison combina habilidades de frontend y diseño para crear soluciones web completas. Su pasión por el código limpio y sus estudios de ingeniería en diseño y entretenimiento digital se refleja en cada proyecto que toca con mucha dedicación.",
            "image": "images/yeisson.png"
        }
    ]

    def display_team_members():
        cols = st.columns(4)
        for i, member in enumerate(team_members):
            img_src = img_to_bytes(member['image'])
            with cols[i]:
                st.markdown(f"""
                <div class="team-card glassy-card animate-fade-in" style="animation-delay: {i * 0.2}s;">
                    <img src="{img_src}" class="member-img" alt="{member['name']}">
                    <h3 class="member-name" style="color: #FFF">{member['name']}</h3>
                    <p class="member-role">{member.get('role', '')}</p>
                    <p class="member-bio" style="color: white;">{member['bio']}</p>
                </div>
                """, unsafe_allow_html=True)

    display_team_members()

    st.markdown("<h2 style='text-align: center; margin-top: 3rem; margin-bottom: 2rem;'>Nuestros Logros</h2>", unsafe_allow_html=True)

    stats_cols = st.columns(4)

    with stats_cols[0]:
        st.markdown("""
        <div class="glassy-card">
            <h3 style="font-size: 1.5rem; font-weight: 700; color: white;">End Devices</h3>
            <p>Completamos la configuración de múltiples end devices a través de platformio</p>
        </div>
        """, unsafe_allow_html=True)

    with stats_cols[1]:
        st.markdown("""
        <div class="glassy-card">
            <h3 style="font-size: 1.5rem; font-weight: 700; color: white;">ETL</h3>
            <p>Logramos hacer extracción, transformación y carga de datos, utilizando diversas técnicas de interpolación con python</p>
        </div>
        """, unsafe_allow_html=True)

    with stats_cols[2]:
        st.markdown("""
        <div class="glassy-card">
            <h3 style="font-size: 1.5rem; font-weight: 700; color: white;">Nube</h3>
            <p>Utilizamos la nube de aws para construir clientes y brokers para soluciones de IOT</p>
        </div>
        """, unsafe_allow_html=True)

    with stats_cols[3]:
        st.markdown("""
        <div class="glassy-card">
            <h3 style="font-size: 1.5rem; font-weight: 700; color: white;">Visualización</h3>
            <p>Realizamos visualicaciones orientadas al entendimiento del usuario con ayuda de Streamlit</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="footer">
        <img src="{img_to_bytes('images/upb.png')}" style="width: 300px; display: block; margin: 0 auto;">
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### Visitantes")
    count = st.sidebar.empty()
    current_count = random.randint(200, 300)
    count.metric("Visitantes hoy", current_count)
