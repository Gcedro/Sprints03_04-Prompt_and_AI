
from src.rag.loader import load_documents
from src.rag.chunking import split_documents
from src.rag.vector_store import create_vector_store

def main():
    documents = load_documents()
    chunks = split_documents(documents)

    if not chunks:
        print("Nenhum trecho foi gerado.")
        return

    create_vector_store(chunks)

    print("Indexação concluída!")
    print(f"Documentos carregados: {len(documents)}")
    print(f"Trechos gerados: {len(chunks)}")

if __name__ == "__main__":
    main()