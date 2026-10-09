
import json
from datetime import datetime
from pathlib import Path

from src.rag.retriever import search_documents

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_FILE = ROOT / "evals" / "perguntas.json"
RESULTS_DIR = ROOT / "evals" / "results"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

with QUESTIONS_FILE.open("r", encoding="utf-8") as file:
    questions = json.load(file)

results = []

for item in questions:
    question = item["question"]
    print(f"\nPergunta: {question}")

    try:
        docs = search_documents(question)

        sources = sorted({
            doc.metadata.get("source", "Fonte desconhecida")
            for doc in docs
        })

        contexts = [
            {
                "source": doc.metadata.get("source", "Fonte desconhecida"),
                "page": doc.metadata.get("page"),
                "text": doc.page_content,
            }
            for doc in docs
        ]

        result = {
            "question": question,
            "expected_behavior": item["expected_behavior"],
            "retrieved_count": len(docs),
            "sources": sources,
            "contexts": contexts,
            "manual_review": {
                "score": None,
                "notes": "Preencher após revisar a recuperação e a resposta do modelo."
            },
        }

        print(f"Trechos recuperados: {len(docs)}")
        print(f"Fontes: {sources or 'Nenhuma'}")

    except Exception as error:
        result = {
            "question": question,
            "error": f"{type(error).__name__}: {error}",
        }
        print("ERRO:", result["error"])

    results.append(result)

output = RESULTS_DIR / (
    f"iteration_{datetime.now():%Y%m%d_%H%M%S}.json"
)

with output.open("w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

print(f"\nResultados salvos em: {output}")
print("Atenção: os resultados precisam de revisão humana.")