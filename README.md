# DataBuddy

Assistente virtual com Inteligência Artificial para auxiliar estudantes e estagiários no aprendizado de Engenharia de Dados.

O DataBuddy utiliza uma base de conhecimento sobre conceitos e tecnologias da área para fornecer explicações claras, didáticas e adequadas ao contexto da pergunta.

## 🎯 Objetivo

O objetivo do DataBuddy é auxiliar estudantes e estagiários de Engenharia de Dados a compreender conceitos, ferramentas e tecnologias da área por meio de explicações simples e didáticas.

O assistente busca facilitar o aprendizado, esclarecer dúvidas e ajudar a pessoa usuária a avançar nos estudos de acordo com seu nível de conhecimento.

## 💡 Problema

Estudantes e iniciantes em Engenharia de Dados podem encontrar dificuldades para compreender conceitos, ferramentas e tecnologias da área.

Além disso, diferentes níveis de conhecimento exigem explicações diferentes. Uma dúvida simples pode acabar recebendo uma explicação muito complexa, dificultando o aprendizado.

O DataBuddy foi criado para oferecer um apoio inicial nesses estudos, utilizando Inteligência Artificial junto a uma base de conhecimento direcionada para Engenharia de Dados.


## ⚙️ Funcionamento

O DataBuddy funciona a partir da combinação entre uma base de conhecimento e um modelo de Inteligência Artificial.

O fluxo da aplicação é:

1. A pessoa usuária envia uma pergunta.
2. A aplicação carrega a base de conhecimento.
3. A pergunta é combinada com as instruções do DataBuddy e com a base de conhecimento.
4. O prompt completo é enviado para o modelo Gemini.
5. O Gemini gera uma resposta de acordo com as instruções definidas.
6. A resposta é apresentada para a pessoa usuária.

### Fluxo

```text
Usuário
   ↓
Pergunta
   ↓
Aplicação Python
   ↓
Base de conhecimento
   ↓
Prompt do DataBuddy
   ↓
Gemini
   ↓
Resposta


## 🛠️ Tecnologias utilizadas

- **Python** — linguagem utilizada no desenvolvimento da aplicação.
- **Google Gemini** — modelo de Inteligência Artificial utilizado para gerar as respostas.
- **Google GenAI SDK** — biblioteca utilizada para integração com a API do Gemini.
- **Markdown** — utilizado na documentação e na base de conhecimento.
- **Git e GitHub** — utilizados para versionamento e organização do projeto.

## 📚 Base de conhecimento

A base de conhecimento do DataBuddy foi criada em Markdown e contém conceitos fundamentais de Engenharia de Dados.

Atualmente, os principais temas são:

- **SQL**
  - SELECT
  - WHERE
  - JOIN
  - GROUP BY
  - WHERE x HAVING
  - Chaves primárias e estrangeiras

- **Python para Dados**
  - Variáveis e tipos de dados
  - Listas e dicionários
  - Pandas
  - NumPy

- **ETL e ELT**
  - Conceitos
  - Etapas
  - Diferenças
  - Exemplos de utilização
  - Qualidade dos dados

- **Spark e PySpark**
  - Processamento distribuído
  - DataFrames
  - Transformações e ações
  - Lazy Evaluation
  - Particionamento
  - Spark SQL

- **Databricks**
  - Lakehouse
  - Data Lake e Data Warehouse
  - Delta Lake
  - Databricks SQL
  - Notebooks
  - Jobs e Workflows
  - Unity Catalog