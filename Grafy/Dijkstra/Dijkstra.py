import networkx as nx
import matplotlib.pyplot as plt

graph_for_Dijkstra = {
    1: [(2, 4), (3, 2)],
    2: [(4, 5)],
    3: [(4, 1)],
    4: [(5, 3)],
    5: [(6, 1)],
    6: []
}


def dijkstra(graph, start):
    dist = [float('inf') for _ in range(1, len(graph) + 1)]
    dist[start - 1] = 0
    queue = [i for i in range(1, len(graph) + 1)]

    while queue:

        min_distance = float('inf')
        node = -1
        for i in queue:
            if dist[i - 1] < min_distance:
                min_distance = dist[i - 1]
                node = i

        queue.remove(node)

        for neighbour in graph[node]:
            if dist[neighbour[0] - 1] > dist[node - 1] + neighbour[1]:
                dist[neighbour[0] - 1] = dist[node - 1] + neighbour[1]
    return dist


print(dijkstra(graph_for_Dijkstra, 1))

G = nx.DiGraph()

for node, neighbors in graph_for_Dijkstra.items():
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
