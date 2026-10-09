# Relatório de evolução do RAG — Sprint 4

## 1. Objetivo

Evoluir o chatbot desenvolvido nas Sprints 1, 2 e 3 para um sistema baseado em Retrieval-Augmented Generation (RAG), capaz de consultar documentos, recuperar informações relevantes e apresentar respostas fundamentadas em fontes documentais.

## 2. Arquitetura implementada

O pipeline foi organizado nas seguintes etapas:

1. **Carregamento:** extração do texto de arquivos PDF usando PyMuPDFLoader.
2. **Chunking:** divisão dos documentos em trechos com RecursiveCharacterTextSplitter.
3. **Embeddings:** representação vetorial dos trechos usando o modelo de embeddings configurado.
4. **Armazenamento:** persistência dos vetores no ChromaDB.
5. **Recuperação:** busca semântica dos trechos relevantes para cada pergunta.
6. **Geração:** envio do contexto recuperado ao modelo de linguagem por meio de um prompt RAG.

## 3. Decisões técnicas

A configuração inicial de chunking utiliza `chunk_size=800` e `chunk_overlap=120`. A recuperação utiliza `k=4`, buscando quatro trechos relevantes por pergunta.

Esses parâmetros são valores iniciais e deverão ser comparados experimentalmente. A configuração final será escolhida com base na relevância do contexto, na fidelidade das respostas e na qualidade das citações.

## 4. Grounding e segurança

O prompt orienta o modelo a responder somente com informações sustentadas pelo contexto recuperado, citar as fontes utilizadas e admitir quando a base não contém informação suficiente.

O contexto documental é tratado como dado não confiável, e não como instrução. Essa medida reduz riscos de prompt injection, mas precisa ser complementada por testes e validações.

## 5. Avaliação

A avaliação considera:

* Faithfulness: fidelidade da resposta ao contexto recuperado.
* Answer relevancy: relevância da resposta em relação à pergunta.
* Qualidade das citações: correspondência entre afirmações, documentos e páginas.
* Segurança: comportamento diante de instruções maliciosas.
* Recusa: comportamento diante de perguntas sem suporte documental.

Os scores serão registrados após a execução e revisão dos casos de teste. Não serão apresentados resultados sem evidência experimental.

## 6. Problemas e soluções

**Problema 1 — documentos extensos:** documentos completos podem ultrapassar o contexto disponível ao modelo.
**Solução proposta:** dividir os documentos em trechos com sobreposição e recuperar apenas os mais relevantes.

**Problema 2 — respostas sem fundamentação:** modelos podem gerar informações que não aparecem na base documental.
**Solução proposta:** reforçar as instruções de grounding, apresentar fontes e avaliar a fidelidade das respostas.

**Problema 3 — instruções maliciosas em documentos:** conteúdo recuperado pode conter comandos destinados a manipular o modelo.
**Solução proposta:** tratar documentos como dados não confiáveis e testar casos específicos de prompt injection.

## 7. Comparação entre iterações

| Iteração | Alteração                                         | Resultado                  |
| -------- | ------------------------------------------------- | -------------------------- |
| 1        | Prompt inicial e configuração inicial de chunking | A preencher após avaliação |
| 2        | Prompt com reforço de segurança                   | A preencher após avaliação |

## 8. Conclusão

A arquitetura proposta permite separar a recuperação documental da geração de respostas, facilitando a atualização da base de conhecimento e a avaliação da qualidade das informações apresentadas.

A conclusão sobre a melhoria de qualidade dependerá dos resultados medidos, da comparação entre modelos e da validação da interface integrada.

## 9. Identificação da equipe

* Integrantes: [preencher]
* RM: [preencher]
* Turma: [preencher]
* Responsabilidades: [preencher]
