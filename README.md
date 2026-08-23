# Resolução de Problemas com Grafos

## Descrição

Este projeto implementa, em Python, um grafo não direcionado que
representa as fronteiras entre as Unidades Federativas (UFs) do Brasil.

Cada UF é representada por um vértice e cada fronteira compartilhada
entre duas UFs é representada por uma aresta.

O projeto foi desenvolvido para a disciplina **Resolução de
Problemas com Grafos**.

## Objetivos

O programa realiza as seguintes tarefas:

-   Representa o grafo a partir dos conjuntos de vértices e arestas;
-   Constrói a **matriz de adjacência**;
-   Constrói a **lista de adjacência**;
-   Constrói a **lista indexada**, utilizando as estruturas α (alfa) e β
    (beta);
-   Calcula o **grau de cada vértice**;
-   Identifica o **grau máximo e mínimo**;
-   Identifica todas as UFs empatadas nos graus máximo e mínimo;
-   Lista os vizinhos das UFs de grau máximo e mínimo;
-   Calcula a **frequência dos graus**;
-   Gera um gráfico com a distribuição da frequência dos graus.

## Estrutura do grafo

### Vértices

Os 27 vértices correspondem às Unidades Federativas do Brasil:

``` text
AC, AL, AP, AM, BA, CE, DF, ES, GO,
MA, MT, MS, MG, PA, PB, PR, PE, PI,
RJ, RN, RS, RO, RR, SC, SP, SE, TO
```

### Arestas

Cada aresta representa uma fronteira compartilhada entre duas UFs.

Exemplo:

``` python
("AC", "AM")
```

Como o grafo é **não direcionado**, `AC — AM` representa a mesma relação
que `AM — AC`. Por isso, cada fronteira é armazenada apenas uma vez no
conjunto de arestas.

## Representações utilizadas

### Matriz de adjacência

É uma matriz 27 × 27.

-   `1` indica que existe uma fronteira entre duas UFs;
-   `0` indica que não existe fronteira.

Como o grafo é não direcionado, a matriz é simétrica.

### Lista de adjacência

Cada UF possui uma lista contendo seus vizinhos.

Exemplo:

``` text
AC -> AM, RO
```

### Lista indexada

A lista indexada utiliza duas estruturas:

-   **α (alfa):** indica a posição inicial dos vizinhos de cada vértice;
-   **β (beta):** armazena os vizinhos em uma sequência única.

Essa representação é construída a partir da lista de adjacência.

## Resultados obtidos

### Graus dos vértices

O grau de um vértice corresponde à quantidade de vizinhos que ele
possui.

Os resultados calculados pelo programa são:

    Grau   Frequência
  ------ ------------
       1            2
       2            6
       3            6
       4            3
       5            4
       6            3
       7            2
       8            1

### Grau máximo

``` text
Grau: 8
UF: BA

Vizinhos:
AL, ES, GO, MG, PE, PI, SE, TO
```

### Grau mínimo

``` text
Grau: 1
UFs: AP, RS

AP -> PA
RS -> SC
```

## Tecnologias utilizadas

-   **Python 3**
-   **Matplotlib** --- geração do gráfico da frequência dos graus
-   **Collections (Counter)** --- contagem da frequência dos graus

## Instalação

É recomendado utilizar um ambiente virtual (`.venv`).

Com o ambiente virtual ativado, instale o Matplotlib:

``` bash
python -m pip install matplotlib
```

## Como executar

Com o ambiente virtual ativado, execute:

``` bash
python trabalho.py
```

O programa exibirá no terminal:

1.  A lista de adjacência;
2.  A matriz de adjacência;
3.  A lista indexada (α e β);
4.  Os graus dos vértices;
5.  O grau máximo e mínimo;
6.  Os vizinhos dos vértices de grau máximo e mínimo;
7.  A frequência dos graus.

Ao final, será exibido o gráfico da frequência dos graus.

## Estrutura do projeto

``` text
Trabalho 01/
│
├── .venv/
└── trabalho.py
```

A implementação foi mantida em um único arquivo Python, organizada em
funções para facilitar a leitura e a compreensão do código.
