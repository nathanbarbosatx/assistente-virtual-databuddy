# Base de Conhecimento - DataBuddy

## Objetivo

Esta base contém conceitos introdutórios e intermediários de Engenharia de Dados. As respostas devem ser claras, didáticas e baseadas somente nas informações deste arquivo.

## SQL

### O que é SQL?

SQL (Structured Query Language) é uma linguagem utilizada para consultar, inserir, atualizar e excluir dados em bancos de dados relacionais. Em Engenharia de Dados, SQL é usado para consultar, transformar, validar e analisar informações.

### SELECT

O comando `SELECT` consulta dados de uma ou mais tabelas.

```sql
SELECT nome, idade
FROM alunos;
```

### WHERE

A cláusula `WHERE` filtra registros de acordo com uma condição.

```sql
SELECT nome, idade
FROM alunos
WHERE idade >= 18;
```

### JOIN

`JOIN` combina informações de duas ou mais tabelas por meio de uma condição de relacionamento, normalmente uma chave.

- `INNER JOIN`: retorna registros com correspondência nas duas tabelas.
- `LEFT JOIN`: retorna todos os registros da tabela da esquerda e as correspondências da tabela da direita.
- `RIGHT JOIN`: retorna todos os registros da tabela da direita e as correspondências da tabela da esquerda.
- `FULL JOIN`: retorna registros das duas tabelas, inclusive os que não possuem correspondência.

```sql
SELECT clientes.nome, pedidos.id_pedido
FROM clientes
INNER JOIN pedidos
    ON clientes.id_cliente = pedidos.id_cliente;
```

### GROUP BY

`GROUP BY` agrupa registros com valores iguais em uma ou mais colunas. É frequentemente usado com funções como `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`.

```sql
SELECT departamento, COUNT(*)
FROM funcionarios
GROUP BY departamento;
```

### WHERE e HAVING

`WHERE` filtra registros antes do agrupamento. `HAVING` filtra resultados depois do `GROUP BY`.

```sql
SELECT departamento, COUNT(*)
FROM funcionarios
GROUP BY departamento
HAVING COUNT(*) > 5;
```

### Chaves primárias e estrangeiras

A chave primária (`PRIMARY KEY`) identifica unicamente cada registro de uma tabela. A chave estrangeira (`FOREIGN KEY`) referencia uma chave de outra tabela e estabelece um relacionamento entre elas.

### SQL na Engenharia de Dados

SQL é comum em processos de ETL e ELT, Data Warehouses, Data Lakes com suporte a SQL e ferramentas de processamento de dados.

## Python para Dados

### O que é Python?

Python é uma linguagem de alto nível com sintaxe simples e diversas bibliotecas para análise, processamento e manipulação de dados. Pode ser usada para automatizar tarefas, manipular arquivos e criar pipelines.

### Variáveis e tipos de dados

Tipos comuns em Python:

- `int`: números inteiros;
- `float`: números decimais;
- `str`: textos;
- `bool`: valores booleanos;
- `list`: coleção ordenada;
- `dict`: estrutura de chave e valor.

### Listas

Listas armazenam vários valores em uma única estrutura.

```python
idades = [20, 21, 25, 30]
print(idades[0])
```

### Dicionários

Dicionários armazenam informações no formato de chave e valor.

```python
aluno = {
    "nome": "Joao",
    "idade": 20,
}
```

### Pandas

Pandas é uma biblioteca Python para manipulação e análise de dados. Seu principal objeto é o `DataFrame`, uma estrutura semelhante a uma tabela.

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Joao"],
    "idade": [20, 22],
}

df = pd.DataFrame(dados)
print(df)
```

### NumPy

NumPy é uma biblioteca para operações numéricas e manipulação de arrays. Ela serve de base para várias ferramentas de análise e processamento de dados.

```python
import numpy as np

numeros = np.array([10, 20, 30, 40])
print(numeros)
```

### Python na Engenharia de Dados

Python pode ser usado para:

- ler arquivos;
- transformar dados;
- validar a qualidade dos dados;
- automatizar tarefas;
- criar pipelines;
- integrar sistemas;
- processar dados com Spark e PySpark.

## ETL e ELT

### ETL

ETL significa Extract, Transform, Load. Nesse processo, os dados são extraídos de uma fonte, transformados e depois carregados em um destino.

1. Extract: obtenção dos dados na fonte.
2. Transform: tratamento, correção ou modificação dos dados.
3. Load: envio dos dados transformados ao destino.

```text
Arquivo CSV -> Extracao -> Transformacao -> Data Warehouse
```

### ELT

ELT significa Extract, Load, Transform. Os dados são extraídos e carregados no destino primeiro; a transformação acontece depois, dentro do ambiente de armazenamento ou processamento.

```text
Fonte de dados -> Extracao -> Carga -> Data Lake ou Data Warehouse -> Transformacao
```

### Diferença entre ETL e ELT

- ETL: `Extract -> Transform -> Load`.
- ELT: `Extract -> Load -> Transform`.

A escolha depende do projeto, das ferramentas e da capacidade de processamento do destino.

### Qualidade dos dados

Durante processos ETL e ELT, é importante verificar problemas como:

- valores nulos;
- registros duplicados;
- tipos de dados incorretos;
- valores fora do padrão esperado;
- registros incompletos.

## Spark e PySpark

### Apache Spark

Apache Spark é um framework de processamento distribuído para grandes volumes de dados. Ele divide o processamento entre recursos de um cluster.

É usado para transformação de dados, processamento em lote, streaming, construção de pipelines e consultas SQL.

### Processamento distribuído

Processamento distribuído divide uma tarefa entre diferentes recursos para que partes do trabalho sejam executadas em paralelo.

```text
Grande conjunto de dados
          |
          v
       Apache Spark
          |
     +----+----+----+
     |    |    |    |
     v    v    v    v
   No 1  No 2  No 3  No 4
```

### PySpark

PySpark é a interface do Apache Spark para Python.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Exemplo") \
    .getOrCreate()

df = spark.read.csv("dados.csv", header=True)
df.show()
```

### DataFrame do Spark

O `DataFrame` do Spark organiza dados em linhas e colunas, de forma semelhante a uma tabela.

```python
df = spark.read.csv("clientes.csv", header=True)
df.select("nome", "idade").show()
```

### Transformações e ações

Transformações criam novas operações e normalmente são avaliadas de forma tardia. Exemplos: `select`, `filter`, `groupBy` e `join`.

Ações executam o processamento e retornam um resultado. Exemplos: `show`, `count` e `collect`.

### Lazy Evaluation

Lazy Evaluation significa que o Spark não executa imediatamente algumas transformações. Ele constrói um plano de execução e processa os dados quando uma ação é chamada.

```python
df_filtrado = df.filter(df.idade > 18)
df_filtrado.show()
```

### Particionamento

Particionamento divide os dados em partes menores que podem ser processadas de forma distribuída.

- `repartition()` altera a quantidade de partições e normalmente redistribui os dados.
- `coalesce()` é usado principalmente para reduzir partições e pode evitar uma redistribuição completa.

```python
df = df.repartition(4)
df = df.coalesce(2)
```

### Spark SQL

Spark SQL permite consultar dados processados pelo Spark usando SQL.

```python
df.createOrReplaceTempView("clientes")

resultado = spark.sql("""
SELECT nome, idade
FROM clientes
WHERE idade >= 18
""")

resultado.show()
```

## Databricks

### O que é Databricks?

Databricks é uma plataforma de dados e inteligência artificial baseada no conceito de Lakehouse. Ela integra recursos de Engenharia de Dados, análise, Machine Learning e Apache Spark.

### Lakehouse

Lakehouse combina a flexibilidade de armazenamento de um Data Lake com recursos de gerenciamento e análise normalmente associados a Data Warehouses.

- Data Lake: armazena grandes volumes de dados em diferentes formatos.
- Data Warehouse: armazena dados estruturados preparados para análise e consultas.

### Delta Lake

Delta Lake adiciona confiabilidade e gerenciamento a Data Lakes, oferecendo:

- transações ACID;
- controle de versões;
- consulta de versões anteriores;
- maior confiabilidade na escrita;
- atualização e exclusão de dados.

### Databricks SQL

Databricks SQL permite executar consultas, analisar dados, criar dashboards, trabalhar com tabelas e explorar informações armazenadas na plataforma.

### Notebooks

Notebooks são ambientes interativos para desenvolver e executar código. No Databricks, podem usar Python, SQL, Scala e R para explorar dados, testar consultas, criar pipelines e documentar análises.

### Jobs e Workflows

Jobs e Workflows automatizam tarefas e organizam processos em etapas.

```text
Leitura -> Validacao -> Transformacao -> Carga -> Relatorio
```

### Unity Catalog

Unity Catalog fornece recursos de governança e gerenciamento de dados no Databricks, incluindo controle de acesso, organização, permissões, descoberta e acompanhamento de informações.

### Databricks na Engenharia de Dados

Databricks pode ser usado para ingestão, transformação, processamento distribuído, criação de pipelines, armazenamento, consultas SQL, automação e governança de dados.
