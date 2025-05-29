import streamlit as st
import pandas as pd
import random
import datetime
import requests

# --- Direcciones correctas ---
ORION_URL = "http://10.38.32.137:5026/v2/entities"
QUANTUMLEAP_URL = "http://10.38.32.137:5068/v2/entities"
HEADERS = {"Accept": "application/json"}

def obtener_sensores():
    try:
        response = requests.get(ORION_URL, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            st.session_state.conexion_exitosa = True
            st.toast("✅ Conexión exitosa con Orion", icon="🟢")
            return response.json()
        else:
            raise Exception("Fallo la petición real")
    except:
        st.session_state.conexion_exitosa = False
        st.toast("⚠️ Sin conexión a Orion. Mostrando datos simulados.", icon="📡")
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
            return pd.DataFrame({"fecha": fechas, "valor": valores})
        else:
            raise Exception("Histórico no disponible")
    except:
        fechas = [datetime.datetime.now() - datetime.timedelta(hours=i) for i in range(10)][::-1]
        valores = [round(random.uniform(20, 60), 2) for _ in range(10)]
        return pd.DataFrame({"fecha": fechas, "valor": valores})

def show_visualizacion():
    if "conexion_exitosa" not in st.session_state:
        st.session_state.conexion_exitosa = True

    st.markdown("## 📈 Visualización de Datos de Sensores")
    sensores = obtener_sensores()
    sensor_ids = [s["id"] for s in sensores]

    seleccion = st.selectbox("Selecciona un sensor o ver todos:", ["Selecciona..."] + sensor_ids + ["Ver todos"])

    if seleccion != "Selecciona...":
        if seleccion == "Ver todos":
            st.markdown("### 📋 Tabla de sensores disponibles")
            datos_tabla = []
            for s in sensores:
                attr = next((k for k in s.keys() if k not in ["id", "type"]), "-")
                val = s.get(attr, {}).get("value", "-")
                datos_tabla.append({
                    "ID": s["id"],
                    "Tipo": s["type"],
                    "Atributo": attr,
                    "Valor actual": val
                })
            st.dataframe(pd.DataFrame(datos_tabla), use_container_width=True)
        else:
            sensor_data = next(s for s in sensores if s["id"] == seleccion)
            atributos = [k for k in sensor_data.keys() if k not in ["id", "type"]]
            atributo_principal = atributos[0] if atributos else None

            tabs = st.tabs(["📍 Estado del Sensor", "📊 Historial", "🧾 Información"])

            with tabs[0]:
                st.markdown("### 📍 Estado del Sensor")

                if atributo_principal:
                    df_hist = obtener_datos_historicos(seleccion, atributo_principal)
                    if not df_hist.empty:
                        valor_actual = df_hist.iloc[-1]["valor"]
                        promedio = round(df_hist["valor"].mean(), 2)
                        delta = round(valor_actual - promedio, 2)

                        st.metric(label=f"{atributo_principal} actual", value=valor_actual, delta=delta)
                        st.metric(label=f"Promedio (últimos 10)", value=promedio)

                        # Obtener tipo de sensor
                        tipo = sensor_data.get("type", "").lower()

                        # Rango por tipo
                        if tipo == "temperatura":
                            bajo, alto = 10, 35
                            unidad = "°C"
                        elif tipo == "humedad":
                            bajo, alto = 30, 70
                            unidad = "%"
                        elif tipo == "luminosidad":
                            bajo, alto = 100, 800
                            unidad = "lx"
                        else:
                            bajo, alto = 20, 80
                            unidad = ""

                        # Evaluación del estado
                        st.markdown("#### 🧠 Evaluación del estado del sensor")
                        if valor_actual < bajo:
                            st.warning(f"🟦 El valor es **muy bajo** para un sensor de {tipo}.")
                        elif valor_actual > alto:
                            st.error(f"🟥 El valor es **muy alto** para un sensor de {tipo}.")
                        else:
                            st.success(f"🟩 El valor está dentro del rango normal para {tipo}.")

                    else:
                        st.warning("No hay datos históricos disponibles.")
                else:
                    st.info("Este sensor no tiene atributos disponibles.")

                # Mostrar tabla de rangos personalizada
                st.markdown("#### 📘 Rangos de referencia")

                tabla_rangos = {
                    "temperatura": ["< 10", "10 – 35", "> 35"],
                    "humedad": ["< 30", "30 – 70", "> 70"],
                    "luminosidad": ["< 100", "100 – 800", "> 800"],
                    "otros": ["< 20", "20 – 80", "> 80"]
                }

                rangos = tabla_rangos.get(tipo, tabla_rangos["otros"])
                st.table(pd.DataFrame({
                    "Estado": ["🟦 Bajo", "🟩 Normal", "🟥 Alto"],
                    "Rango": rangos,
                    "Descripción": [
                        "Valor muy bajo para este tipo de sensor.",
                        "El sensor está operando en condiciones aceptables.",
                        "Valor muy alto para este tipo de sensor."
                    ]
                }))



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
