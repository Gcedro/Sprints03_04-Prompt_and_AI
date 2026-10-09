
from src.rag.loader import load_documents
from src.rag.chunking import split_documents

documents = load_documents()
chunks = split_documents(documents)

print("\nPrimeiro trecho:")
print(chunks[0].page_content[:500])
print("\nFonte:")
print(chunks[0].metadata)