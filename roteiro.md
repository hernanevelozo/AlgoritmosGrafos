# Trabalho Prático - Algoritmos em Grafos

## Integrantes:
- Gustavo Valadares Castro
- Hernane Velozo Rosa
- João Victor Martins
- Pedro Igor dos Reis

## Tutorial de instalação
### Configurações do ambiente de desenvolvimento:
- **Sistema Operacional**: Ubuntu 22.04.2 LTS x86_64
- **Versão do Python**: 3.10.10
- **Versão do Pip**: 23.0.1
- **Versão da networkx**: 3.1

### Passo a passo para execução do programa:
- Instalar e configurar o **Python** (preferencialmente a versão 3.10) na sua máquina. Caso não esteja instalado ou configurado, visite: [https://www.python.org/downloads/](https://www.python.org/downloads/) para mais informações
- Instalar e configurar o gerenciador de pacotes **Pip**. Para mais informações, acesse: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)
- No terminal do sistema, execute o comando a seguir, para instalar o biblioteca **networkx**:

```
pip install networkx
```

- Para executação do programa, escreva a seguir. Certifique-se de que você esteja no diretório **src**.
```
python main.py
```

## Descrição das funções utilizadas no networkx
`nx.DiGraph()`: A estrutura de dados que compõe nx.DiGraph() é uma combinação de listas de adjacência e dicionários. Cada vértice do digrafo é representado como uma chave no dicionário, e o valor associado a cada chave é uma lista de vértices para os quais há um arco saindo do vértice correspondente.

`DiGraph.out_degree()`: O algoritmo executado nessa função percorre as arestas do digrafo e conta o número de arestas que possuem o vértice fornecido como origem. Ele retorna esse número como o grau de saída do vértice.

`DiGraph.in_degree()`: O algoritmo executado na função percorre as arestas do digrafo e conta o número de arestas que têm o vértice fornecido como destino. Ele retorna esse número como o grau de entrada do vértice.

`DiGraph.successors()`: O algoritmo executado é um loop simples que percorre as arestas do digrafo para encontrar todos os vértices que são alcançáveis a partir do vértice fornecido como parâmetro, seguindo as arestas que saem desse vértice.

`DiGraph.predecessors()`: O algoritmo executado nessa função se trata de um loop percorre as arestas do digrafo para encontrar todos os vértices que têm uma aresta direcionada para o vértice fornecido como parâmetro.

`nx.is_strongly_connected()`: O algoritmo implementado nessa função é baseado na busca em profundidade (DFS) e verifica se um grafo direcionado é fortemente conectado.

`nx.is_directed_acyclic_graph()`: O algoritmo executado nessa função é conhecido como "algoritmo de verificação de grafo direcionado acíclico (DAG)". Nele, é realizada uma verificação topológica para determinar se existe uma ordenação dos vértices do grafo tal que todas as arestas apontem para vértices anteriores na ordenação.

**Observação:** O que se procura saber no enunciado é se o grafo é cíclico. Portanto, o retorno da função deve ter a lógica invertida. 

## Resultados obtidos
### Arquivo 1 
```
9 12
1 2
1 3
2 3
2 4
3 4
4 5
5 6
5 7
6 7
6 8
7 8
9 7
```
Saída para vértice **6**:
```
Informações do vértice:  6
Grau de saída:  2
Grau de entrada:  1
Conjunto de sucessores:  [7, 8]
Conjunto de predecessores:  [5]
Busca em profundidade:  [6, 8, 7]
Busca em largura:  [6, 7, 8]
Informações do grafo:
Número de vértices:  9
Número de arestas:  12
É conexo?  Não
É cíclico?  Não
```

### Arquivo 2
```
7 9
1 2
1 3
2 3
2 4
3 4
4 5
5 6
5 7
6 7
```
Saída para vértice **5**:
```
Informações do vértice:  5
Grau de saída:  2
Grau de entrada:  1
Conjunto de sucessores:  [6, 7]
Conjunto de predecessores:  [4]
Busca em profundidade:  [5, 7, 6]
Busca em largura:  [5, 6, 7]
Informações do grafo:
Número de vértices:  7
Número de arestas:  9
É conexo?  Não
É cíclico?  Não
```
