import json
import time
from flask import Flask, render_template, Response
from models import buscar_ultimas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    def gerar():
        while True:
            rows = buscar_ultimas(50)
            dados = [
                {
                    "device": row[0],
                    "temp": row[1],
                    "umidade": row[2],
                    "criado_em": row[3].strftime("%H:%M:%S")
                }
                for row in rows
            ]
            yield f"data: {json.dumps(dados)}\n\n"
            time.sleep(2)

    return Response(gerar(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)