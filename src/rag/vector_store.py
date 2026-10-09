
from pathlib import Path
from langchain_chroma import Chroma

from src.rag.embeddings import get_embeddings

PERSIST_DIRECTORY = Path("data/chroma")
COLLECTION_NAME = "goodwe_knowledge"


def create_vector_store(chunks):
    PERSIST_DIRECTORY.mkdir(parents=True, exist_ok=True)

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(PERSIST_DIRECTORY),
    )

    if chunks:
        vector_store.add_documents(chunks)

    return vector_store


def load_vector_store():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(PERSIST_DIRECTORY),
    )