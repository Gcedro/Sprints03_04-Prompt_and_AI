
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.rag.retriever import get_retriever
from src.rag.prompt_rag import RAG_TEMPLATE


def format_context(documents):
    """Monta o contexto com as fontes e páginas."""
    parts = []

    for doc in documents:
        source = doc.metadata.get("source", "Fonte desconhecida")
        page = doc.metadata.get("page")

        # PyMuPDFLoader normalmente numera as páginas a partir de zero.
        page_label = f", página {page + 1}" if isinstance(page, int) else ""

        parts.append(
            f"[Fonte: {source}{page_label}]\n{doc.page_content}"
        )

    return "\n\n".join(parts)


def answer_question(question, llm, k=4):
    """Recupera documentos e gera uma resposta fundamentada."""
    documents = get_retriever(k=k).invoke(question)

    if not documents:
        return (
            "Não encontrei essa informação nos documentos disponíveis."
        )

    context = format_context(documents)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=RAG_TEMPLATE,
    )

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question,
    })

    return answer