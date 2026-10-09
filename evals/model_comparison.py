
import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from src.rag.chain import answer_question

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_FILE = ROOT / "evals" / "perguntas.json"
RESULTS_DIR = ROOT / "evals" / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Configure os modelos disponíveis no seu provedor.
# Estes nomes são exemplos: confirme se existem no seu ambiente.
MODELS = [
    {
        "name": os.getenv("RAG_MODEL_A", "modelo-a"),
        "temperature": 0,
        "top_p": 0.9,
        "max_tokens": 500,
    },
    {
        "name": os.getenv("RAG_MODEL_B", "modelo-b"),
        "temperature": 0,
        "top_p": 0.9,
        "max_tokens": 500,
    },
]

with QUESTIONS_FILE.open("r", encoding="utf-8") as file:
    questions = json.load(file)

results = []

for config in MODELS:
    print(f"\nTestando modelo: {config['name']}")

    llm = ChatOllama(
        model=config["name"],
        temperature=config["temperature"],
        top_p=config["top_p"],
        num_predict=config["max_tokens"],
    )

    for item in questions:
        record = {
            "model": config["name"],
            "parameters": config,
            "question": item["question"],
            "expected_behavior": item["expected_behavior"],
            "prompt_version": "2.0",
        }

        try:
            answer = answer_question(item["question"], llm)

            record["answer"] = answer
            record["status"] = "completed"

            print(f"\nPergunta: {item['question']}")
            print(f"Resposta: {answer}")

        except Exception as error:
            record["status"] = "error"
            record["error"] = f"{type(error).__name__}: {error}"
            print(f"Erro: {record['error']}")

        results.append(record)

output = RESULTS_DIR / (
    f"model_comparison_{datetime.now():%Y%m%d_%H%M%S}.json"
)

with output.open("w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

print(f"\nResultados salvos em: {output}")
print("Revise as respostas antes de atribuir notas.")