
import os

from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

app = Flask(__name__, static_folder=None)

MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model=MODEL,
    base_url=BASE_URL,
    temperature=0.2
)

DADOS_GOODWE = """
GW-01: disponível, potência atual 0 kW,
limite de 22 kW, energia 0 kWh.

GW-02: em uso, potência atual 22 kW,
limite de 22 kW, energia 45 kWh.

GW-03: offline.
"""

PROMPT = """
Você é o GoodWe AI, assistente especializado em
carregamento de veículos elétricos e gerenciamento
de energia GoodWe.

Responda em português brasileiro, de forma clara.
Não invente dados operacionais.
Se não souber uma informação, diga isso claramente.
Para questões fora do tema GoodWe, energia e
veículos elétricos, informe educadamente seu escopo.

Dados operacionais disponíveis:
""" + DADOS_GOODWE


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"reply": "Digite uma mensagem."}), 400

        response = llm.invoke(
            PROMPT + "\n\nPergunta do usuário:\n" + message
        )

        return jsonify({"reply": response.content})

    except Exception as error:
        print("Erro no chatbot:", error)
        return jsonify({
            "reply": "Não consegui gerar a resposta. "
                     "Confira se o Ollama está funcionando "
                     "e se o modelo está instalado."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
