
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """Divide os documentos em trechos para busca semântica."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        add_start_index=True,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(documents)

    print(f"Trechos gerados: {len(chunks)}")

    return chunks