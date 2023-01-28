import networkx as nx

# Crear un grafo no dirigido
G = nx.Graph()

# Agregar los planetas
planetas = ["Tierra", "Knowhere", "Zen-Whoberi", "Vomir", "Titán", "Nidavellir", "Planeta1", "Planeta2", "Planeta3", "Planeta4", "Planeta5", "Planeta6"]
G.add_nodes_from(planetas)

# Agregar las aristas
G.add_edge("Tierra", "Knowhere", weight=20)
G.add_edge("Tierra", "Zen-Whoberi", weight=30)
G.add_edge("Tierra", "Vomir", weight=40)
G.add_edge("Knowhere", "Titán", weight=10)
G.add_edge("Knowhere", "Nidavellir", weight=15)
G.add_edge("Zen-Whoberi", "Planeta1", weight=25)
G.add_edge("Zen-Whoberi", "Planeta2", weight=35)
G.add_edge("Vomir", "Planeta3", weight=45)
G.add_edge("Vomir", "Planeta4", weight=55)
G.add_edge("Titán", "Planeta5", weight=5)
G.add_edge("Titán", "Planeta6", weight=10)
# Encontrar el árbol de expansión mínima
arbol_expansion = nx.prim_mst(G)

# Hallar el camino más corto desde Tierra hasta Vormir
camino1 = nx.dijkstra_path(G, "Tierra", "Vomir")

# Hallar el camino más corto desde Knowhere hasta Titán
camino2 = nx.dijkstra_path(G, "Knowhere", "Titán")

# Hallar el camino más corto desde Zen-
shortest_path = nx.dijkstra_path(G, "Zen-Whoberi", "Nidavellir")

# Obtener todos los vecinos de Titán
vecinos_de_titan = G.neighbors("Titán")