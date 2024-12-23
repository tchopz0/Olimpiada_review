import networkx as nx
import matplotlib.pyplot as plt

graph_for_Bellman_Ford = {
    1: [(2, -4), (3, 2)],
    2: [(4, -5)],
    3: [(4, 1)],
    4: [(5, -3)],
    5: [(6, 1)],
    6: []
}


def bellmanFord(g, start):
    dist = [float('inf') for _ in range(1, len(g) + 1)]
    dist[start - 1] = 0

    for _ in range(len(g) - 1):
        for neighbour in g:
            for v, weight in g[neighbour]:                          # silly
                if dist[neighbour - 1] + weight < dist[v - 1]:
                    dist[v - 1] = dist[neighbour - 1] + weight

    # brakuje sprawdzenia nieskonczonych wezlow jeszce (zakładam że jest to graf acykliczny)
    return dist

print(bellmanFord(graph_for_Bellman_Ford, 1))


G = nx.DiGraph()

for node, neighbors in graph_for_Bellman_Ford.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

pos = {
    1: (0, 2),
    2: (1, 2),
    3: (0, 1),
    4: (1, 1),
    5: (0, 0),
    6: (1, 0)
}

plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Graph For Dijkstra")
plt.axis('off')
plt.show()
