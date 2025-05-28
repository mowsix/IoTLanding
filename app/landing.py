import streamlit as st

def show_landing():
    # Configuración de la página principal
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
