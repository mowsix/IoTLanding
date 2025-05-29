import streamlit as st
import requests
import pandas as pd
from crud import crear_sensor, subscribir_sensor, eliminar_sensor

# --- Configuración de conexión Orion ---
ORION_URL = "http://10.38.32.137:5026/v2/entities"
HEADERS = {"Accept": "application/json"}

# --- Obtener sensores desde Orion o fallback ---
def obtener_sensores():
    try:
        response = requests.get(ORION_URL, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            st.toast("✅ Conexión exitosa con el servidor Orion.", icon="🟢")
            return response.json()
        else:
            st.toast("⚠️ No se pudo obtener la lista de sensores desde el servidor.", icon="⚠️")
            return []
    except Exception:
        st.toast("🔌 Sin conexión al servidor Orion. Mostrando datos simulados.", icon="📡")
        return [
            {"id": "sensor_w_ht_001", "type": "humedad", "valor": {"type": "Float", "value": 24.5}},
            {"id": "sensor_l_rs_001", "type": "temperatura", "valor": {"type": "Float", "value": 25.0}}
        ]

# --- Mostrar tabla con lectura dinámica ---
def mostrar_tabla_sensores(data, filtro):
    if not data:
        st.warning("No hay sensores disponibles.")
        return pd.DataFrame()

    rows = []
    for sensor in data:
        id_sensor = sensor.get("id", "")
        tipo = sensor.get("type", "")
        nombre = id_sensor.split("_")[-1] if "_" in id_sensor else id_sensor

        # Buscar el campo con valor
        lectura_valor = ""
        for k, v in sensor.items():
            if k not in ("id", "type") and isinstance(v, dict) and "value" in v:
                lectura_valor = v["value"]
                campo = k
                break
        else:
            campo = "N/A"

        rows.append({
            "ID": id_sensor,
            "Tipo": tipo,
            "Nombre": nombre,
            "Campo": campo,
            "Lectura": lectura_valor
        })

    df = pd.DataFrame(rows)

    if filtro:
        df = df[df["ID"].str.contains(filtro, case=False) | df["Nombre"].str.contains(filtro, case=False)]

    st.dataframe(df, use_container_width=True)
    return df

# --- Vista principal de gestión ---
def show_sensores():
    st.markdown("## 📊 Panel de Gestión de Sensores")

    if "show_form" not in st.session_state:
        st.session_state.show_form = None

    col1, _ = st.columns([1, 2])
    with col1:
        if st.button("➕ Crear Sensor"):
            st.session_state.show_form = "crear"
        if st.button("🔔 Suscribir Sensor"):
            st.session_state.show_form = "suscribir"
        if st.button("🗑️ Eliminar Sensor"):
            st.session_state.show_form = "eliminar"

    st.markdown("---")

    # --- Crear Sensor ---
    if st.session_state.show_form == "crear":
        with st.expander("📝 Crear un nuevo sensor", expanded=True):
            with st.form("crear_form"):
                sensor_id = st.text_input("ID del sensor (ej: sensor_ht_001)").strip()
                tipo_sensor = st.selectbox("Tipo de sensor", ["humedad", "temperatura", "luminosidad"])
                nombre_atributo = st.text_input("Nombre del campo de lectura (ej: valor)").strip()
                valor = st.number_input("Valor inicial", value=25.0)

                if st.form_submit_button("Crear"):
                    if not sensor_id or not nombre_atributo:
                        st.warning("Por favor completa todos los campos.")
                    else:
                        try:
                            crear_sensor(sensor_id=sensor_id, campo=nombre_atributo, valor=valor, tipo=tipo_sensor)
                            st.toast("✅ Sensor creado exitosamente.", icon="✅")
                        except Exception as e:
                            st.toast(f"❌ Error al conectar con el servidor: {e}", icon="⚠️")

    # --- Suscribir Sensor ---
    elif st.session_state.show_form == "suscribir":
        with st.expander("🔔 Suscribir un sensor existente", expanded=True):
            sensores = obtener_sensores()
            filtro = st.text_input("🔎 Buscar sensor por ID o nombre", key="filtro_subs")
            df = mostrar_tabla_sensores(sensores, filtro)

            if not df.empty:
                with st.form("suscribir_form"):
                    sensor_id = st.text_input("ID completo del sensor a suscribir", key="subs").strip()
                    seleccionar = st.selectbox("Seleccionar de la tabla para suscribir:", ["Selecciona..."] + df["ID"].tolist())
                    if st.form_submit_button("Suscribir"):
                        try:
                            id_final = seleccionar if seleccionar != "Selecciona..." else sensor_id
                            if id_final:
                                subscribir_sensor(id_final.replace("urn:ngsi-ld:Sensor:", ""))
                                st.toast(f"🔔 Sensor '{id_final}' suscrito correctamente.", icon="✅")
                            else:
                                st.warning("Debes ingresar un ID o seleccionar uno de la tabla.")
                        except Exception:
                            st.toast("❌ No se pudo suscribir el sensor. Verifica la conexión.", icon="⚠️")

    # --- Eliminar Sensor ---
    elif st.session_state.show_form == "eliminar":
        with st.expander("🗑️ Eliminar un sensor", expanded=True):
            sensores = obtener_sensores()
            filtro = st.text_input("🔎 Buscar sensor por ID o nombre")
            df = mostrar_tabla_sensores(sensores, filtro)

            if not df.empty:
                with st.form("eliminar_form"):
                    sensor_id = st.text_input("ID completo del sensor a eliminar", key="del").strip()
                    eliminar_desde_tabla = st.selectbox("Eliminar directamente desde la tabla:", ["Selecciona..."] + df["ID"].tolist())
                    if st.form_submit_button("Eliminar"):
                        try:
                            id_final = eliminar_desde_tabla if eliminar_desde_tabla != "Selecciona..." else sensor_id
                            if id_final:
                                eliminar_sensor(id_final.replace("urn:ngsi-ld:Sensor:", ""))
                                st.toast(f"🗑️ Sensor '{id_final}' eliminado correctamente.", icon="✅")
                            else:
                                st.warning("Debes ingresar un ID o seleccionar uno de la tabla.")
                        except Exception:
                            st.toast("❌ No se pudo eliminar el sensor. Verifica la conexión.", icon="⚠️")
