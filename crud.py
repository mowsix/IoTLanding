import requests
import streamlit as st

# --- Configuración de Orion y QuantumLeap ---
ORION_URL = "http://10.38.32.137:5026/v2"
QUANTUMLEAP_URL = "http://10.38.32.137:5068/v2/notify"

HEADERS = {
    "Content-Type": "application/json"
}

# --- Crear sensor ---
def crear_sensor(sensor_id: str, campo: str, valor: float, tipo: str = "Sensor"):
    """
    Crea un sensor con ID y atributo dinámico.
    Ejemplo de campo: 'valor', 'temperatura', 'humedad', etc.
    """
    entidad = {
        "id": f"{sensor_id}",
        "type": tipo,
        campo: {
            "type": "Float",
            "value": round(valor, 2),
            "metadata": {}
        }
    }

    try:
        response = requests.post(f"{ORION_URL}/entities", json=entidad, headers=HEADERS)
        if response.status_code == 201:
            st.success(f"✅ Sensor '{sensor_id}' creado exitosamente con atributo '{campo}'.")
        else:
            st.error(f"❌ Error al crear sensor: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error de conexión al crear sensor: {e}")

# --- Suscribir sensor ---
def subscribir_sensor(sensor_id: str):
    """
    Crea una suscripción en Orion para un sensor existente.
    """
    urn_id = f"{sensor_id}"
    suscripcion = {
        "description": f"Suscripción para {sensor_id}",
        "subject": {
            "entities": [
                {"id": urn_id, "type": "Sensor"}
            ],
            "condition": {
                "attrs": ["valor"]  # Cambiar si usas otro campo
            }
        },
        "notification": {
            "http": {
                "url": QUANTUMLEAP_URL
            },
            "attrs": ["valor"]
        },
        "expires": "2040-01-01T14:00:00.00Z",
        "throttling": 5
    }

    try:
        response = requests.post(f"{ORION_URL}/subscriptions", json=suscripcion, headers=HEADERS)
        if response.status_code in (201, 204):
            st.success(f"🔔 Sensor '{sensor_id}' suscrito correctamente.")
        else:
            st.error(f"❌ Error al suscribir sensor: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error de conexión al suscribir sensor: {e}")

# --- Eliminar sensor ---
def eliminar_sensor(sensor_id: str):
    """
    Elimina una entidad de sensor en Orion v2.
    """
    urn_id = f"{sensor_id}"
    try:
        response = requests.delete(f"{ORION_URL}/entities/{urn_id}")
        if response.status_code == 204:
            st.success(f"🗑️ Sensor '{sensor_id}' eliminado correctamente.")
        elif response.status_code == 404:
            st.warning(f"⚠️ El sensor '{sensor_id}' no existe.")
        else:
            st.error(f"❌ Error al eliminar sensor: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error de conexión al eliminar sensor: {e}")
