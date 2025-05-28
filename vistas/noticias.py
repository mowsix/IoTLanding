import streamlit as st
from PIL import Image
import io
import base64

def render_news_card(title, date, description, image_path, delay=0):
    image = Image.open(image_path)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    img_str = base64.b64encode(img_bytes).decode()
    return f"""
    <div class="news-card glassy-card animate-fade-in" style="animation-delay: {delay}s;">
        <img class="news-image" src="data:image/jpeg;base64,{img_str}" />
        <div class="news-content">
            <div class="news-date">{date}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
    </div>
    """

def show_news():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        * {
            font-family: 'Poppins', sans-serif;
        }

        .header-container {
            background: linear-gradient(135deg, #D50032 0%, #FF4081 100%);
            padding: 3rem 0;
            text-align: center;
            border-radius: 0 0 2rem 2rem;
            margin-bottom: 2rem;
            animation: fadeIn 1s ease-in-out;
        }

        .news-header {
            color: white !important;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            align-items: center;
        }

        .news-subheader {    
            color: rgba(255, 255, 255, 0.9) !important;
            font-weight: 300 !important;
            max-width: 700px;
            margin: 0 auto !important;
            font-size: 1.2rem !important;
        }

        .glassy-card {
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.05);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
            color: white;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .glassy-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }

        .news-card {
            display: flex;
            flex-direction: row;
            gap: 20px;
            align-items: center;
        }

        .news-image {
            width: 200px;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
            border: 3px solid white;
        }

        .news-content {
            flex-grow: 1;
        }

        .news-date {
            font-size: 14px;
            color: #ffeb3b;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .cta-button {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, rgb(198, 17, 177) 0%, #FF4081 100%);
            color: white !important;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            margin-top: 2rem;
        }

        .cta-button:hover {
            background: linear-gradient(135deg, #00796B 0%, #004D40 100%);
            transform: translateY(-2px);
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

    # Header con botón
    st.markdown("""
    <div class="header-container">
        <h1 class="news-header">Últimas Noticias</h1>
        <p class="news-subheader">Mantente al día con las actualizaciones y logros de nuestro proyecto de IOT.</p>
        <a href="#" class="cta-button">Contáctanos</a>
    </div>
    """, unsafe_allow_html=True)

    # Noticias
    news_cards = [
        {"title": "Smart Living Lab", "date": "Mayo 2025", "description": "Es un laboratorio vivo (vivienda sostenible) de aprovechamiento energético que surgió de un diseño bioclimático y cuenta con un área de 80 m².", "image_path": "images/ecovilla.png"},
        {"title": "Casa inteligente", "date": "Junio 2025", "description": "Es un proyecto que busca resultados globales, que busca impacto, que busca solución de problemas reales y que busca sensibilizar al ciudadano en el uso de las energías renovables, de las tecnologías eficientes, de la mitigación de emisiones por el uso de estos elementos.", "image_path": "images/casainteligente.jpg"},
        {"title": "End Devices", "date": "Junio 2025","description": "La primera etapa del proyecto de IOT ya fue desplegada, todos los end devices ya estan listos para ser usados", "image_path": "images/lora.png"},
    ]

    for i, news_card in enumerate(news_cards):
        st.markdown(render_news_card(
            news_card["title"], 
            news_card["date"], 
            news_card["description"], 
            news_card["image_path"],
            delay=i * 0.2
        ), unsafe_allow_html=True)


