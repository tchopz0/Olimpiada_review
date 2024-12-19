import networkx as nx
import matplotlib.pyplot as plt

# Tworzymy nowy graf
G = nx.DiGraph()

# Dodajemy krawędzie z wagami (numeracja od 1)
edges = {
    1: [(2, -4), (3, 2)],
    2: [(4, -5)],
    3: [(4, 1)],
    4: [(5, -3)],
    5: [(6, 1)],
    6: []
}

# Dodanie krawędzi do grafu
for node, neighbors in edges.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Ustawienie układu grafu (pozycje wierzchołków)
pos = {
    1: (0, 2),
    2: (1, 2),
    3: (0, 1),
    4: (1, 1),
    5: (0, 0),
    6: (1, 0)
}

# Rysowanie grafu
plt.figure(figsize=(8, 6))

# Rysowanie wierzchołków i krawędzi
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray')

# Rysowanie wag na krawędziach
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Wyświetlanie grafu
plt.title("Graf z numeracją od 1")
plt.axis('off')
plt.show()
