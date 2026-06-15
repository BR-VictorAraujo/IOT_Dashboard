import json
import paho.mqtt.client as mqtt
from config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC
from models import criar_tabela, salvar_leitura

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado ao broker MQTT!")
        client.subscribe(MQTT_TOPIC)
        print(f"Escutando tópico: {MQTT_TOPIC}")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        dados = json.loads(payload)
        print(f"Mensagem recebida: {dados}")

        device = dados.get("device", "desconhecido")
        temp = dados.get("temp", 0.0)
        umidade = dados.get("umidade", 0.0)

        salvar_leitura(device, temp, umidade)
        print(f"Salvo no banco: {device} | {temp}°C | {umidade}%")

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

criar_tabela()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT)
client.loop_forever()