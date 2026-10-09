# Histórico de versões do prompt RAG

## Versão 1.0 — inicial

* Respostas baseadas no contexto recuperado.
* Recusa quando não há informação documental suficiente.
* Solicitação de citação de documento e página.
* Orientação para responder em português brasileiro.

## Versão 2.0 — reforço de segurança

* Contexto explicitamente tratado como dados, não como instruções.
* Instruções documentais que tentem alterar o comportamento devem ser ignoradas.
* Reforço contra invenção de especificações técnicas.
* Exigência de que a citação sustente a afirmação apresentada.

## Validação

As mudanças são hipóteses de melhoria. A versão 2.0 só deverá ser considerada superior após testes com as mesmas perguntas da versão anterior, revisão das citações e comparação das métricas registradas em `evals/results/`.
