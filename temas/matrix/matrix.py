# Representar un grafo como matriz de adyacencia
import numpy as np

# Nodos: A, B, C, D
nodos = ['A', 'B', 'C', 'D']

# Crear la matriz de adyacencia
matriz_adyacencia = np.array([
    [0, 1, 1, 0],  # A
    [1, 0, 1, 0],  # B
    [1, 1, 0, 1],  # C
    [0, 0, 1, 0]   # D
])

# Imprimir la matriz
print("Matriz de Adyacencia:")
print(matriz_adyacencia)

# Nodos conectados desde A
nodo_inicio = 'A'
indice_inicio = nodos.index(nodo_inicio)
conexiones = [nodos[i] for i, conectado in enumerate(matriz_adyacencia[indice_inicio]) if conectado == 1]

print(f"El nodo {nodo_inicio} está conectado con: {', '.join(conexiones)}")

