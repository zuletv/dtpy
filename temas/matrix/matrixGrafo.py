import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo desde una matriz de adyacencia ponderada
matriz_ponderada = [
    [0, 4, 2, 0],
    [4, 0, 1, 3],
    [2, 1, 0, 5],
    [0, 3, 5, 0]
]

# Crear el grafo
grafo = nx.Graph()

# Agregar nodos
nodos = ['A', 'B', 'C', 'D']
for i in range(len(nodos)):
    for j in range(len(nodos)):
        if matriz_ponderada[i][j] != 0:
            grafo.add_edge(nodos[i], nodos[j], weight=matriz_ponderada[i][j])

# Dibujar el grafo
pos = nx.spring_layout(grafo)  # Posición de los nodos
nx.draw(grafo, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=12)
labels = nx.get_edge_attributes(grafo, "weight")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
plt.title("Grafo Ponderado")
plt.show()
"""
Sin ponderar: Nodos conectados con líneas simples.
Ponderado: Nodos conectados con líneas etiquetadas con valores (pesos).

"""
