import streamlit as st
import pandas as pd
import random
import datetime
import requests

ORION_URL = "http://10.38.32.137:5026/ngsi-ld/entities"
QUANTUMLEAP_URL = "http://10.38.32.137:5068/v2/entities"
HEADERS = {"Accept": "application/ld+json"}

def obtener_sensores():
    try:
        response = requests.get(ORION_URL, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            st.session_state.conexion_exitosa = True
            return response.json()
        else:
            raise Exception("Fallo la petición real")
    except:
        st.session_state.conexion_exitosa = False
        return [
            {"id": "urn:ngsi-ld:Sensor:001", "type": "Sensor", "RS": {"value": 23.5}},
            {"id": "urn:ngsi-ld:Sensor:002", "type": "Sensor", "HT": {"value": 45.2}},
            {"id": "urn:ngsi-ld:Sensor:003", "type": "Sensor", "MS": {"value": 78.9}}
        ]

def obtener_datos_historicos(sensor_id, atributo):
    try:
        url = f"{QUANTUMLEAP_URL}/{sensor_id}/attrs/{atributo}?limit=10"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            valores = [x["value"] for x in data["values"]]
            fechas = [datetime.datetime.fromisoformat(x["recvTime"][:-1]) for x in data["index"]]
            df = pd.DataFrame({"fecha": fechas, "valor": valores})
            return df
        else:
            raise Exception("Histórico no disponible")
    except:
        st.session_state.conexion_exitosa = False
        fechas = [datetime.datetime.now() - datetime.timedelta(hours=i) for i in range(10)][::-1]
        valores = [round(random.uniform(20, 60), 2) for _ in range(10)]
        return pd.DataFrame({"fecha": fechas, "valor": valores})

def show_visualizacion():
    if "conexion_exitosa" not in st.session_state:
        st.session_state.conexion_exitosa = True

    st.markdown("## 📈 Visualización de Datos de Sensores")
    sensores = obtener_sensores()
    sensor_ids = [s["id"] for s in sensores]

    if not st.session_state.conexion_exitosa:
        st.toast("No se logró conexión con el servidor. Se muestran datos simulados.", icon="⚠️")

    seleccion = st.selectbox("Selecciona un sensor o ver todos:", ["Selecciona..."] + sensor_ids + ["Ver todos"])

    if seleccion != "Selecciona...":
        if seleccion == "Ver todos":
            st.markdown("### 📋 Tabla de sensores disponibles")
            datos_tabla = []
            for s in sensores:
                attr = next((k for k in s.keys() if k not in ["id", "type"]), "-")
                val = s.get(attr, {}).get("value", "-")
                datos_tabla.append({"ID": s["id"], "Tipo": s["type"], "Atributo": attr, "Valor": val})
            st.dataframe(pd.DataFrame(datos_tabla))
        else:
            sensor_data = next(s for s in sensores if s["id"] == seleccion)
            atributos = [k for k in sensor_data.keys() if k not in ["id", "type"]]
            atributo_principal = atributos[0] if atributos else None

            tabs = st.tabs(["📍 Estado del Sensor", "📊 Historial", "🧾 Información"])

            with tabs[0]:
                st.markdown("### 📍 Estado del Sensor")
                if atributo_principal:
                    df_hist = obtener_datos_historicos(seleccion, atributo_principal)
                    valor_actual = df_hist.iloc[-1]["valor"]
                    promedio = round(df_hist["valor"].mean(), 2)
                    diferencia = valor_actual - promedio
                    st.metric(label=f"{atributo_principal} actual", value=valor_actual, delta=round(diferencia, 2))
                    st.metric(label=f"Promedio (últimos 10)", value=promedio)
                else:
                    st.info("Este sensor no tiene atributos disponibles.")

            with tabs[1]:
                st.markdown("### 📊 Historial de datos")
                if atributo_principal:
                    df_hist = obtener_datos_historicos(seleccion, atributo_principal)
                    st.line_chart(df_hist.rename(columns={"fecha": "index"}).set_index("index"))
                else:
                    st.warning("No hay atributo principal para graficar.")

            with tabs[2]:
                st.markdown("### 🧾 Información del Sensor")
                st.json(sensor_data)
