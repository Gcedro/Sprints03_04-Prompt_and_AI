
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings

load_dotenv()


def get_embeddings():
    api_key = os.getenv("OLLAMA_API_KEY")

    if not api_key:
        raise ValueError(
            "Configure OLLAMA_API_KEY no arquivo .env"
        )

    return OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="https://ollama.com",
        client_kwargs={
            "headers": {
                "Authorization": f"Bearer {api_key}"
            }
        },
    )