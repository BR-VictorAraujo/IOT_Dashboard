import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leituras (
            id        SERIAL PRIMARY KEY,
            device    VARCHAR(50),
            temp      FLOAT,
            umidade   FLOAT,
            criado_em TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def salvar_leitura(device, temp, umidade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leituras (device, temp, umidade) VALUES (%s, %s, %s)",
        (device, temp, umidade)
    )
    conn.commit()
    cursor.close()
    conn.close()

def buscar_ultimas(limite=50):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT device, temp, umidade, criado_em FROM leituras ORDER BY criado_em DESC LIMIT %s",
        (limite,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows