import matplotlib.pyplot as plt
import networkx as nx

# Tworzymy graf
G = nx.DiGraph()

# Dodajemy wierzchołki i krawędzie
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('G', 'J'), ('G', 'K'), ('G', 'L'),
    ('D', 'H'),
    ('I', 'M')
])

# Ręczne przypisanie pozycji wierzchołków (identyczne jak w grafie)
pos = {
    'A': (0, 4),
    'B': (-2, 3),
    'C': (0, 2),
    'D': (2, 2),
    'E': (-2, 1),
    'F': (-1, 1),
    'G': (1, 1),
    'H': (2, 1),
    'I': (2, 0),
    'J': (0.5, 0),
    'K': (0.5, -0.5),
    'L': (1.5, -0.5),
    'M': (2, -1)
}

# Rysowanie grafu
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
plt.title("Graf w układzie hierarchicznym")
plt.show()
