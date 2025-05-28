import streamlit as st

def show_landing():
    st.markdown("""<style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #F5F5F5;
        }

        .header {
            padding: 1rem;
            background: linear-gradient(90deg, #D50032, #FF4081);
            color: white !important;
            border-radius: 8px;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo-title h2 {
            margin: 0;
            font-size: 1.8rem;
        }

        .glass-card {
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        }

        .footer {
            padding: 2rem 0;
            background-color: #F5F5F5;
            color: #D50032;
            text-align: center;
            margin-top: 3rem;
            font-weight: 500;
            border-top: 1px solid #eaeaea;
        }

        .glass-list li {
            margin-bottom: 0.8rem;
            font-size: 1.05rem;
        }

        .glass-list span {
            font-weight: 600;
            color: #D50032;
        }
    </style>""", unsafe_allow_html=True)

    # --- Encabezado
    st.markdown("""
    <div class="header">
        <div class="logo-title">
            <h2>📡 Universidad Pontificia Bolivariana</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Bienvenida
    st.markdown("## 👋 Bienvenido al Proyecto de Sensores Ambientales")
    st.markdown("Este proyecto tiene como objetivo monitorear variables ambientales mediante sensores distribuidos en la sede de la Universidad.")
    st.divider()

    # --- Sección ¿Qué encontrarás aquí?
    st.markdown("""
    <div class="glass-card">
        <h4 style="color:white; font-weight: 700;">🔍 ¿Qué encontrarás aquí?</h4>
        <ul class="glass-list">
        <li><span style="color:white; font-weight: 600;">Información General:</span> objetivos, el equipo y el impacto del proyecto.</li>
        <li><span style="color:white; font-weight: 600;">Visualizaciones:</span> datos ambientales capturados por sensores en tiempo real.</li>
        <li><span style="color:white; font-weight: 600;">Autenticación:</span> acceso seguro para funcionalidades de análisis y gestión.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- Imágenes destacadas
    st.markdown("## 🖼️ Imágenes destacadas")

    imagenes = [
        "images/image1.jpg",        # Imagen 1
        "images/image2.jpeg",         # Imagen 2
        "images/image4.jpg"          # Imagen 3
    ]

    cols = st.columns(3)
    for col, img in zip(cols, imagenes):
        with col:
            st.image(img, use_container_width=True)

    # --- Footer
    st.markdown("""
    <div class='footer'>© 2025 Universidad Pontificia Bolivariana – Proyecto de Monitoreo Ambiental IoT</div>
    """, unsafe_allow_html=True)
