# Avaliação do RAG — Sprint 4

## Iteração 1 — configuração inicial

**Configuração:** divisão de documentos com `chunk_size=800`, `chunk_overlap=120` e recuperação com `k=4`.

**Objetivo:** verificar a recuperação de trechos relevantes, a identificação das fontes e o comportamento diante de perguntas sem resposta na base documental.

**Procedimento:** executar `python evals/run_evaluation.py` e revisar os trechos recuperados em `evals/results/`.

**Métricas e revisão:**

* Relevância do contexto recuperado: avaliar manualmente.
* Faithfulness: avaliar se a resposta final é sustentada pelos documentos.
* Answer relevancy: avaliar se a resposta atende à pergunta.
* Citações: verificar se as fontes citadas sustentam as afirmações.

**Limitação:** os scores ainda não foram medidos. Não registrar valores até executar os testes e revisar os resultados.

## Iteração 2 — a realizar

Modificar a configuração de chunking ou o valor de `k`, executar novamente as mesmas perguntas e comparar os resultados. Registrar a mudança, os resultados observados e a decisão final.
