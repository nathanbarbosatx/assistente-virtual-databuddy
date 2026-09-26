# Base de Conhecimento — DataBuddy

## SQL

### O que é SQL?

SQL (Structured Query Language) é uma linguagem utilizada para consultar, inserir, atualizar e excluir dados em bancos de dados relacionais.

É muito utilizada em Engenharia de Dados para consultar e manipular informações armazenadas em tabelas.

### SELECT

O comando SELECT é utilizado para consultar dados de uma ou mais tabelas.

Exemplo:

SELECT nome, idade
FROM alunos;

Nesse exemplo, são retornadas as colunas nome e idade da tabela alunos.

### WHERE

A cláusula WHERE é utilizada para filtrar registros de acordo com uma condição.

Exemplo:

SELECT nome, idade
FROM alunos
WHERE idade >= 18;

Nesse caso, somente os alunos com idade maior ou igual a 18 anos serão retornados.

### JOIN

JOIN é utilizado para combinar informações de duas ou mais tabelas utilizando uma condição de relacionamento entre elas.

Um exemplo comum é relacionar tabelas por meio de uma chave.

Os principais tipos de JOIN são:

- INNER JOIN: retorna registros que possuem correspondência nas duas tabelas.
- LEFT JOIN: retorna todos os registros da tabela da esquerda e as correspondências encontradas na tabela da direita.
- RIGHT JOIN: retorna todos os registros da tabela da direita e as correspondências encontradas na tabela da esquerda.
- FULL JOIN: retorna registros das duas tabelas, incluindo aqueles que não possuem correspondência.

### GROUP BY

GROUP BY é utilizado para agrupar registros que possuem valores iguais em uma ou mais colunas.

É frequentemente utilizado junto com funções de agregação, como COUNT, SUM, AVG, MIN e MAX.

Exemplo:

SELECT departamento, COUNT(*)
FROM funcionarios
GROUP BY departamento;

Nesse exemplo, os funcionários são agrupados por departamento e a quantidade de funcionários de cada departamento é calculada.

### WHERE x HAVING

WHERE e HAVING são utilizados para filtrar dados, mas em momentos diferentes.

WHERE filtra os registros antes do agrupamento.

HAVING filtra os resultados depois que o GROUP BY foi realizado.

Exemplo:

SELECT departamento, COUNT(*)
FROM funcionarios
GROUP BY departamento
HAVING COUNT(*) > 5;

Nesse caso, somente os departamentos que possuem mais de cinco funcionários serão retornados.

### Chaves primárias e estrangeiras

A chave primária (PRIMARY KEY) identifica de forma única cada registro de uma tabela.

A chave estrangeira (FOREIGN KEY) é utilizada para estabelecer um relacionamento entre tabelas, referenciando uma chave de outra tabela.

Exemplo:

Uma tabela clientes pode possuir a coluna id_cliente como chave primária.

Uma tabela pedidos pode possuir a coluna id_cliente como chave estrangeira, relacionando cada pedido a um cliente.

### SQL no contexto da Engenharia de Dados

Na Engenharia de Dados, SQL pode ser utilizado para consultar, transformar, validar e analisar dados.

Também é comum utilizar SQL em processos de ETL e ELT, Data Warehouses, Data Lakes com suporte a SQL e ferramentas de processamento de dados.


## Python para Dados

### O que é Python?

Python é uma linguagem de programação de alto nível, conhecida por possuir uma sintaxe relativamente simples e por ter diversas bibliotecas voltadas para análise, processamento e manipulação de dados.

Na Engenharia de Dados, Python pode ser utilizado para automatizar tarefas, manipular arquivos, criar pipelines e trabalhar com grandes volumes de dados por meio de ferramentas e bibliotecas específicas.

### Variáveis e tipos de dados

Variáveis são utilizadas para armazenar valores durante a execução de um programa.

Alguns tipos de dados comuns em Python são:

- `int`: números inteiros;
- `float`: números decimais;
- `str`: textos;
- `bool`: valores booleanos, como `True` e `False`;
- `list`: coleção ordenada de elementos;
- `dict`: estrutura composta por pares de chave e valor.

### Listas

Uma lista permite armazenar vários valores em uma única estrutura.

Exemplo:

```python
idades = [20, 21, 25, 30]

## Spark e PySpark

### O que é Apache Spark?

Apache Spark é um framework de processamento distribuído utilizado para processar grandes volumes de dados.

Em vez de depender do processamento de uma única máquina, o Spark pode distribuir o processamento entre diferentes máquinas de um cluster.

Ele é utilizado em tarefas como:

- processamento e transformação de dados;
- análise de grandes volumes de dados;
- construção de pipelines;
- processamento em lote;
- processamento de dados em streaming;
- execução de consultas SQL.

### O que é processamento distribuído?

Processamento distribuído é uma abordagem em que uma tarefa é dividida entre diferentes recursos computacionais para que o processamento possa ser realizado de forma paralela.

No Spark, um cluster pode possuir diferentes máquinas responsáveis por executar partes do processamento.

De forma simplificada:

```text
Grande conjunto de dados
          |
          v
       Apache Spark
          |
     +----+----+----+
     |    |    |    |
     v    v    v    v
   Nó 1  Nó 2  Nó 3  Nó 4




## Databricks

### O que é Databricks?

Databricks é uma plataforma de dados e inteligência artificial baseada no conceito de Lakehouse.

Ela oferece recursos para trabalhar com engenharia de dados, análise de dados, Machine Learning e inteligência artificial em um mesmo ambiente.

A plataforma possui integração com tecnologias como Apache Spark e permite desenvolver e executar processos de dados.

### O que é um Lakehouse?

Lakehouse é uma arquitetura que busca combinar características de Data Lakes e Data Warehouses.

Um Data Lake é utilizado para armazenar grandes volumes de dados em diferentes formatos.

Um Data Warehouse é tradicionalmente utilizado para armazenar dados estruturados preparados para análises e consultas.

A arquitetura Lakehouse busca oferecer flexibilidade de armazenamento de um Data Lake junto a recursos de gerenciamento, qualidade e análise normalmente associados a Data Warehouses.

### Delta Lake

Delta Lake é uma camada de armazenamento utilizada para adicionar recursos de confiabilidade e gerenciamento de dados sobre Data Lakes.

Entre seus recursos estão:

- transações ACID;
- controle de versões dos dados;
- possibilidade de consultar versões anteriores;
- maior confiabilidade durante operações de escrita;
- suporte a operações de atualização e exclusão de dados.

### Databricks e Apache Spark

O Databricks possui integração com Apache Spark.

Isso permite utilizar recursos do Spark para realizar processamento distribuído de dados dentro da plataforma.

Por exemplo, um processo pode utilizar PySpark para ler dados, realizar transformações e gravar os resultados em tabelas ou arquivos.

### Databricks SQL

Databricks SQL permite utilizar SQL para consultar e analisar dados na plataforma.

Ele pode ser utilizado para:

- executar consultas SQL;
- analisar dados;
- criar dashboards;
- trabalhar com tabelas;
- explorar informações armazenadas na plataforma.

### Notebooks

Notebooks são ambientes interativos utilizados para desenvolver e executar código.

No Databricks, notebooks podem ser utilizados com linguagens como Python, SQL, Scala e R.

Eles podem ser utilizados para:

- explorar dados;
- desenvolver transformações;
- testar consultas;
- criar pipelines;
- documentar processos de análise.

### Jobs e Workflows

Jobs e Workflows permitem automatizar a execução de tarefas e processos de dados.

Um processo pode ser organizado em diferentes etapas, permitindo que determinadas tarefas sejam executadas em uma ordem definida.

Por exemplo:

```text
Leitura dos dados
       ↓
Validação
       ↓
Transformação
       ↓
Carga
       ↓
Relatório