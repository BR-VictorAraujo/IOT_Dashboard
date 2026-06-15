# IoT Dashboard — M5StickC + MQTT + PostgreSQL + Flask

Dashboard em tempo real para monitoramento de temperatura via M5StickC Plus 2 (ESP32-S3).

## Arquitetura

M5StickC → Mosquitto (MQTT) → Python → PostgreSQL → Flask → Dashboard

## Tecnologias

- **Hardware:** M5StickC Plus 2 (ESP32-S3)
- **Protocolo:** MQTT via Mosquitto
- **Backend:** Python + Flask
- **Banco de dados:** PostgreSQL
- **Frontend:** HTML + Chart.js + SSE (Server-Sent Events)

## Funcionalidades

- Leitura de temperatura do sensor interno do ESP32
- Publicação via MQTT a cada 3 segundos
- Armazenamento histórico no PostgreSQL
- Dashboard com gráficos atualizados em tempo real
- Alerta visual configurável por limite de temperatura
- Simulador do ESP32 para testes sem hardware

## Como rodar

### 1. Instalar dependências Python

    pip install flask paho-mqtt psycopg2-binary python-dotenv

### 2. Configurar o banco

Edita o config.py com as credenciais do seu PostgreSQL:

    DB_HOST = "IP"
    DB_PORT = "5432"
    DB_NAME = "iot"
    DB_USER = "postgres"
    DB_PASS = "sua_senha"

### 3. Configurar o Mosquitto

Adiciona ao mosquitto.conf:

    listener 1883 0.0.0.0
    allow_anonymous true

### 4. Rodar

    # Terminal 1 — subscriber MQTT
    python mqtt_subscriber.py

    # Terminal 2 — simulador (sem hardware)
    python simulate.py

    # Terminal 3 — dashboard
    python app.py

Acessa: http://localhost:5000

### 5. Hardware (M5StickC Plus 2)

Abre o projeto m5stick-iot no PlatformIO, configura WiFi e IP do broker em main.cpp e faz o upload para o dispositivo.

## Estrutura do projeto

    ├── app.py                 # Flask + SSE
    ├── config.py              # Configurações do ambiente
    ├── models.py              # Conexão e queries PostgreSQL
    ├── mqtt_subscriber.py     # Escuta MQTT e salva no banco
    ├── simulate.py            # Simula o ESP32
    ├── templates/
    │   └── index.html         # Dashboard
    └── m5stick-iot/
        └── src/main.cpp       # Código do ESP32
