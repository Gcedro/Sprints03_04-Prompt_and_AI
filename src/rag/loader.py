
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

KNOWLEDGE_BASE = Path("data/knowledge_base")


def load_documents():
    """Carrega todos os PDFs da base de conhecimento."""
    if not KNOWLEDGE_BASE.exists():
        raise FileNotFoundError(
            f"Pasta não encontrada: {KNOWLEDGE_BASE.resolve()}"
        )

    pdf_files = list(KNOWLEDGE_BASE.rglob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "Nenhum PDF encontrado em data/knowledge_base/"
        )

    documents = []

    for pdf_path in pdf_files:
        loader = PyMuPDFLoader(str(pdf_path))
        pages = loader.load()

        for page in pages:
            page.metadata["source"] = pdf_path.name

        documents.extend(pages)

    print(f"PDFs carregados: {len(pdf_files)}")
    print(f"Páginas carregadas: {len(documents)}")

    return documents