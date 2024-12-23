import matplotlib.pyplot as plt
import networkx as nx

from collections import deque

graphForBfs = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['J'],
    'G': ['K', 'L'],
    'H': [],
    'I': ['M'],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()

        # space for node processing, e.g. print
        print("node: " + str(node))

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)


bfs(graphForBfs, 'A')



G = nx.DiGraph()
edges = [(node, neighbor) for node in graphForBfs for neighbor in graphForBfs[node]]      # refraction to adjacency array "edges"
G.add_edges_from(edges)

pos = {
    'A': (0, 4),
    'B': (-1.5, 2),
    'C': (0, 2),
    'D': (1.5, 2),
    'E': (-2, 1),
    'F': (-1, 1),
    'G': (0, 1),
    'H': (1, 1),
    'I': (2, 1),
    'J': (-1, 0),
    'K': (-0.5, -0.5),
    'L': (0.5, -0.5),
    'M': (2, 0)
}

plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
plt.title("Graph for BFS")
plt.show()








