
from src.rag.vector_store import load_vector_store


def get_retriever(k=4):
    vector_store = load_vector_store()

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )


def search_documents(question, k=4):
    retriever = get_retriever(k=k)
    return retriever.invoke(question)