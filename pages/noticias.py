import streamlit as st

st.set_page_config(page_title="Noticias - UPB")

st.markdown("# 📰 Noticias del Proyecto")

for i in range(3):
    st.markdown(f"""
    <div class="news-card">
        <img class="news-image" src="https://via.placeholder.com/600x180?text=Noticia+{i+1}" />
        <div class="news-content">
            <div class="news-date">Mayo 2025</div>
            <h4>Noticia {i+1}</h4>
            <p>Descripción breve de la noticia {i+1}, relacionada con el proyecto de sensores.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
