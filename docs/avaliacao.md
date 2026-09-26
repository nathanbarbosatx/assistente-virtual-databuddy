# Avaliação e Métricas — DataBuddy

## Objetivo da avaliação

A avaliação do DataBuddy tem como objetivo verificar se o assistente consegue responder dúvidas de Engenharia de Dados de forma clara, relevante e alinhada à sua base de conhecimento.

Também buscamos verificar se o assistente respeita o escopo definido e evita apresentar informações inventadas quando não possui conhecimento suficiente.

## Metodologia de avaliação

Foram realizadas perguntas relacionadas aos principais temas presentes na base de conhecimento do DataBuddy.

Os testes foram feitos diretamente pela aplicação, utilizando o fluxo:

Usuário → Aplicação → Prompt → Gemini → Resposta

As respostas foram analisadas manualmente de acordo com critérios definidos para verificar a qualidade e o comportamento do assistente.

## Critérios de avaliação

Cada resposta foi avaliada considerando os seguintes critérios:

- **Relevância:** verifica se a resposta atende ao que foi perguntado.
- **Clareza:** verifica se a explicação é compreensível para o público-alvo.
- **Fidelidade à base:** verifica se as informações estão de acordo com a base de conhecimento.
- **Escopo:** verifica se a resposta permanece relacionada à Engenharia de Dados.
- **Alucinação:** verifica se o assistente apresentou informações inventadas ou sem fundamentação.

## Resultados dos testes

Foram realizados testes com perguntas relacionadas aos conteúdos disponíveis na base de conhecimento.

| # | Pergunta | Relevância | Clareza | Fidelidade à base | Escopo | Alucinação |
|---|---|---:|---:|---:|---:|---:|
| 1 | O que é SQL? | 1 | 1 | 1 | 1 | 0 |
| 2 | Qual a diferença entre WHERE e HAVING? | 1 | 1 | 1 | 1 | 0 |
| 3 | O que é ETL? | 1 | 1 | 1 | 1 | 0 |
| 4 | Qual a diferença entre ETL e ELT? | 1 | 1 | 1 | 1 | 0 |

### Legenda

- **1:** critério atendido.
- **0:** critério não atendido.
- Para **Alucinação**, `0` significa que não foi identificada informação inventada na resposta.

## Análise dos resultados

Nos testes realizados, todas as respostas atenderam aos critérios de relevância, clareza, fidelidade à base de conhecimento e respeito ao escopo do DataBuddy.

Também não foram identificadas ocorrências de informações inventadas nas respostas analisadas.

Os resultados indicam que, nos cenários testados, o assistente conseguiu utilizar a base de conhecimento para responder dúvidas relacionadas aos conceitos de Engenharia de Dados de forma didática.

## Limitações da avaliação

A avaliação foi realizada com um conjunto pequeno de perguntas e não representa todos os possíveis cenários de uso do DataBuddy.

Os testes foram realizados manualmente e consideraram principalmente perguntas relacionadas aos conteúdos disponíveis na base de conhecimento.

Além disso, o comportamento das respostas pode variar de acordo com a pergunta realizada e com a resposta gerada pelo modelo de inteligência artificial.

Por isso, os resultados apresentados devem ser considerados como uma avaliação inicial do protótipo.

## Conclusão

Os testes realizados demonstraram que o DataBuddy conseguiu responder às perguntas avaliadas de forma relevante, clara e alinhada ao seu objetivo educacional.

Nos quatro testes realizados, todos os critérios definidos foram atendidos e não foram identificadas ocorrências de informações inventadas.

A avaliação também mostrou que a combinação entre uma base de conhecimento estruturada, instruções específicas no prompt e um modelo de inteligência artificial permite construir um assistente direcionado para um contexto específico.

Como próximos passos, a avaliação pode ser ampliada com mais perguntas, diferentes níveis de dificuldade e cenários fora do escopo da base de conhecimento.