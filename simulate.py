import json
import time
import random
import paho.mqtt.client as mqtt
from config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC

client = mqtt.Client()
client.connect(MQTT_HOST, MQTT_PORT)

print("Simulador iniciado! Publicando dados a cada 3 segundos...")
print("Pressione Ctrl+C para parar.\n")

while True:
    payload = {
        "device": "m5stick-simulado",
        "temp": round(random.uniform(22.0, 35.0), 1),
        "umidade": round(random.uniform(40.0, 80.0), 1)
    }

    mensagem = json.dumps(payload)
    client.publish(MQTT_TOPIC, mensagem)
    print(f"Publicado: {mensagem}")

    time.sleep(3)