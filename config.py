import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do banco PostgreSQL
DB_HOST = os.getenv("DB_HOST", "192.168.0.17")  # IP do servidor PostgreSQL
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "iot")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "nwaypro")

# Configurações do broker MQTT
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "iot/temperatura")