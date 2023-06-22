import networkx as nx

def busca_profundidade(grafo, vertice):
    visitados = []
    pilha = [vertice]

    while pilha:
        v = pilha.pop()

        if v not in visitados:
            visitados.append(v)

            for vizinho in grafo.neighbors(v):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return visitados

def busca_largura(grafo, vertice):
    visitados = []
    fila = [vertice]
    
    while fila:
        v = fila.pop(0)
        if v not in visitados:
            visitados.append(v)
            fila.extend(grafo.neighbors(v))
    
    return visitados

# Main
caminho_arquivo, vertice_partida = "", ""
n, m = 0, 0

# Recebe nome do arquivo e vértice por parâmetro do programa
caminho_arquivo = input("Insira o arquivo contendo os componentes do grafo: ")
vertice_partida = int(input("Insira um vértice do arquivo: "))

# Abre o arquivo contendo componentes do grafo
grafo = nx.DiGraph()
with open(caminho_arquivo, 'r') as file:
    # Lê primeira linha: n = n de vértices, m = n de arestas                                                                                 
    n, m = map(int, file.readline().split())

    # A cada linha lida, adicione aresta (v1, v2) ao dígrafo 
    for _ in range(m):
        v_origem, v_destino = map(int, file.readline().split())
        grafo.add_edge(v_origem, v_destino)

# Informações do vértice
print("\n\033[1mInformações do vértice: \033[0m", vertice_partida)                         
print("Grau de saída: ",                grafo.out_degree(vertice_partida))                  # Grau de saída
print("Grau de entrada: ",              grafo.in_degree(vertice_partida))                   # Grau de entrada
print("Conjunto de sucessores: ",       list(grafo.successors(vertice_partida)))            # Conjunto de sucessores
print("Conjunto de predecessores: ",    list(grafo.predecessors(vertice_partida)))          # Conjunto de predecessores
print("Busca em profundidade: ",         list(busca_profundidade(grafo, vertice_partida)))  # Busca em profundidade
print("Busca em largura: ",              list(busca_largura(grafo, vertice_partida)))       # Busca em largura

# Informações do grafo
print("\033[1mInformações do grafo: \033[0m")                         
print("Número de vértices: ", n)
print("Número de arestas: ", m)

resposta = "";
if (nx.is_strongly_connected(grafo)): resposta = "Sim"                      
else: resposta = "Não" 
print("É conexo? ", resposta)                                               # É conexo?

if (not nx.is_directed_acyclic_graph(grafo)): resposta = "Sim"             
else: resposta = "Não" 
print("É cíclico? ", resposta)                                              # É cíclico?
