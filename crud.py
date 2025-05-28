# crud.py
import requests
import streamlit as st

# URL base de Orion Context Broker
ORION_URL = "http://10.38.32.137:5026/ngsi-ld"
QUANTUMLEAP_URL = "http://10.38.32.137:5068/v2/notify"

HEADERS = {
    "Content-Type": "application/ld+json"
}

def crear_sensor(sensor_id: str, campo: str, valor: float):
    """Crear entidad de sensor con atributo dinámico"""
    entidad = {
        "id": sensor_id,
        "type": "Sensor",
        campo: {
            "type": "Float",
            "value": round(valor, 2)
        }
    }

    response = requests.post(f"{ORION_URL}/entities", json=entidad, headers=HEADERS)
    if response.status_code == 201:
        st.success(f"✅ Sensor '{sensor_id}' creado exitosamente con atributo '{campo}'.")
    else:
        st.error(f"❌ Error al crear sensor: {response.status_code} - {response.text}")


def subscribir_sensor(sensor_id: str):
    """Crear una suscripción para un sensor (QuantumLeap o notificación externa)"""
    suscripcion = {
        "type": "Subscription",
        "entities": [{"id": f"urn:ngsi-ld:Sensor:{sensor_id}"}],
        "watchedAttributes": ["temperature"],
        "notification": {
            "endpoint": {
                "uri": QUANTUMLEAP_URL,
                "accept": "application/json"
            }
        }
    }

    response = requests.post(f"{ORION_URL}/subscriptions", json=suscripcion, headers=HEADERS)
    if response.status_code in (201, 204):
        st.success(f"🔔 Sensor '{sensor_id}' suscrito correctamente.")
    else:
        st.error(f"❌ Error al suscribir sensor: {response.status_code} - {response.text}")

def eliminar_sensor(sensor_id: str):
    """Eliminar una entidad de sensor de Orion-LD"""
    sensor_urn = f"urn:ngsi-ld:Sensor:{sensor_id}"
    response = requests.delete(f"{ORION_URL}/entities/{sensor_urn}")
    if response.status_code == 204:
        st.success(f"🗑️ Sensor '{sensor_id}' eliminado.")
    elif response.status_code == 404:
        st.warning(f"⚠️ El sensor '{sensor_id}' no existe.")
    else:
        st.error(f"❌ Error al eliminar sensor: {response.status_code} - {response.text}")
