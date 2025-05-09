from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
from datetime import datetime
import json

app = Flask(__name__)
historico = []  # Guarda as mensagens enviadas do MQTT

# Conecta no broker e se inscreve no tópico onde a mensagem será enviada
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com código de resultado: " + str(rc))
    client.subscribe("led/saida")

# Quando a mensagem chegar no tópico, essa função é chamada
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        estado = payload.get("comando", "desconhecido")
        origem = payload.get("origem", "desconhecida")
    except json.JSONDecodeError:
        estado = msg.payload.decode()  # Pega o conteúdo da mensagem
        origem = "Led Verde"

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Momento da mensagem
    historico.append((estado, origem, timestamp))  # Adiciona o estado e horário no histórico
    print(f"[{timestamp}] LED: {estado.upper()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conexão com o Broker
try:
    client.connect("192.168.0.103", 1883, 60)
    client.loop_start()
except:
    print("⚠️ Não foi possível conectar ao broker MQTT.")

@app.route("/")
def index():
    if historico:
        estado_atual = historico[-1]
    else:
        estado_atual = None
    return render_template("index.html", estado_atual=estado_atual)

# Rota para atualizar o status via AJAX
@app.route("/atualizar_status")
def atualizar_status():
    if historico:
        estado_atual = historico[-1]
        return jsonify({
            'estado': estado_atual[0],
            'hora': estado_atual[2]
        })
    else:
        return jsonify({'estado': None})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
