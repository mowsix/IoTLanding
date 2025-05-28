import streamlit as st
import requests
import pandas as pd
import time
from crud import crear_sensor, subscribir_sensor, eliminar_sensor

ORION_URL = "http://10.38.32.137:5026/ngsi-ld/entities"
HEADERS = {"Accept": "application/ld+json"}

def obtener_sensores():
    try:
        response = requests.get(ORION_URL, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            st.toast("⚠️ No se pudo obtener la lista de sensores desde el servidor.", icon="⚠️")
            return []
    except Exception:
        st.toast("🔌 Sin conexión al servidor Orion. Mostrando datos simulados.", icon="📡")
        return [
            {"id": "urn:ngsi-ld:Sensor:001", "type": "Sensor", "RS": {"type": "Float", "value": 23.4}},
            {"id": "urn:ngsi-ld:Sensor:002", "type": "Sensor", "HT": {"type": "Float", "value": 19.7}},
            {"id": "urn:ngsi-ld:Sensor:003", "type": "Sensor", "MS": {"type": "Float", "value": 31.1}}
        ]

def mostrar_tabla_sensores(data, filtro):
    df = pd.DataFrame(data)
    df["nombre"] = df["id"].apply(lambda x: x.split(":")[-1])
    if filtro:
        df = df[df["id"].str.contains(filtro, case=False) | df["nombre"].str.contains(filtro, case=False)]
    st.dataframe(df[["id", "type", "nombre"]], use_container_width=True)
    return df

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

    if st.session_state.show_form == "crear":
        with st.expander("📝 Crear un nuevo sensor", expanded=True):
            with st.form("crear_form"):
                sensor_id = st.text_input("ID del sensor (ej: urn:ngsi-ld:Sensor:001)")
                nombre_campo = st.selectbox("Nombre del atributo del sensor", ["RS", "HT", "MS"])
                valor = st.number_input("Valor inicial", value=25.0)
                if st.form_submit_button("Crear"):
                    try:
                        crear_sensor(sensor_id=sensor_id, campo=nombre_campo, valor=valor)
                        st.toast("✅ Sensor creado exitosamente.", icon="✅")
                    except Exception:
                        st.toast("❌ Error al conectar con el servidor para crear el sensor.", icon="⚠️")

    elif st.session_state.show_form == "suscribir":
        with st.expander("🔔 Suscribir un sensor existente", expanded=True):
            sensores = obtener_sensores()
            filtro = st.text_input("🔎 Buscar sensor por ID o nombre", key="filtro_subs")
            df = mostrar_tabla_sensores(sensores, filtro)

            with st.form("suscribir_form"):
                sensor_id = st.text_input("ID completo del sensor a suscribir", key="subs")
                seleccionar = st.selectbox("Seleccionar de la tabla para suscribir:", ["Selecciona..."] + df["id"].tolist())
                if st.form_submit_button("Suscribir"):
                    try:
                        if seleccionar != "Selecciona...":
                            subscribir_sensor(seleccionar)
                            st.toast(f"🔔 Sensor '{seleccionar}' suscrito correctamente.", icon="✅")
                        elif sensor_id:
                            subscribir_sensor(sensor_id)
                            st.toast(f"🔔 Sensor '{sensor_id}' suscrito correctamente.", icon="✅")
                        else:
                            st.warning("Debes ingresar un ID o seleccionar uno de la tabla.")
                    except Exception:
                        st.toast("❌ No se pudo suscribir el sensor. Verifica la conexión.", icon="⚠️")

    elif st.session_state.show_form == "eliminar":
        with st.expander("🗑️ Eliminar un sensor", expanded=True):
            sensores = obtener_sensores()
            filtro = st.text_input("🔎 Buscar sensor por ID o nombre")
            df = mostrar_tabla_sensores(sensores, filtro)

            with st.form("eliminar_form"):
                sensor_id = st.text_input("ID completo del sensor a eliminar", key="del")
                eliminar_desde_tabla = st.selectbox("Eliminar directamente desde la tabla:", ["Selecciona..."] + df["id"].tolist())
                if st.form_submit_button("Eliminar"):
                    try:
                        if eliminar_desde_tabla != "Selecciona...":
                            eliminar_sensor(eliminar_desde_tabla)
                            st.toast(f"🗑️ Sensor '{eliminar_desde_tabla}' eliminado correctamente.", icon="✅")
                        elif sensor_id:
                            eliminar_sensor(sensor_id)
                            st.toast(f"🗑️ Sensor '{sensor_id}' eliminado correctamente.", icon="✅")
                        else:
                            st.warning("Debes ingresar un ID o seleccionar uno de la tabla.")
                    except Exception:
                        st.toast("❌ No se pudo eliminar el sensor. Verifica la conexión.", icon="⚠️")
