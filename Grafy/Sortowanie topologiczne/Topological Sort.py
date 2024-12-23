import matplotlib.pyplot as plt
import networkx as nx

graphForTopologicalSort = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: [],
    6: [7],
    7: [8],
    8: [9],
    9: []
}

visited = set()
stack = []

def dfs(node):
    if node not in visited:
        visited.add(node)
    for neighbour in graphForTopologicalSort[node]:
        if neighbour not in visited:
            dfs(neighbour)
    stack.append(node)

for node in graphForTopologicalSort:
    if node not in visited:
        dfs(node)

print(stack[::-1])


G = nx.DiGraph()

edges = [(node, neighbour) for node in graphForTopologicalSort for neighbour in graphForTopologicalSort[node]]
# print(edges)

G.add_edges_from(edges)

pos = {
    1: (0, 4),
    2: (-2, 3),
    3: (2, 4),
    4: (0, 2),
    5: (2, 2),
    6: (-2, 1),
    7: (-0.5, 1),
    8: (1, 1),
    9: (2.5, 1),
}

plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
plt.title("Graph For Topological Sort")
plt.show()
