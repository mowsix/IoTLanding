import streamlit as st

# Datos de login quemados
USER_CREDENTIALS = {
    "admin@upb.edu.co": "12345",
    "usuario@upb.edu.co": "sensor2025",
    "oe": "oe"
}

def login():
    if not st.session_state.get("authenticated"):
        st.markdown("<h2 class='section-title'>Iniciar Sesión</h2>", unsafe_allow_html=True)
        with st.form("login_form"):
            email = st.text_input("Correo Electrónico")
            password = st.text_input("Contraseña", type="password")
            submit = st.form_submit_button("Ingresar")

            if submit:
                if email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password:
                    st.session_state["authenticated"] = True
                    st.session_state["user"] = email
                    st.success("✅ Inicio de sesión exitoso.")
                    st.rerun()  # 🔁 Recarga inmediata para evitar el segundo clic
                else:
                    st.error("❌ Credenciales incorrectas")
    else:
        st.success(f"🔐 Ya has iniciado sesión como: {st.session_state['user']}")
