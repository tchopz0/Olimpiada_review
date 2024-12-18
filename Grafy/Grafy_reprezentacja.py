# Graf jako macierz sąsiedztwa
from collections import deque

INF = float('inf')

# Macierz sąsiedztwa dla grafu z wierzchołkami A, B, C, D, E
# A: 0, B: 1, C: 2, D: 3, E: 4
graph_matrix = [
    [0, 10, 12, 60, INF],  # A
    [INF, 0, 20, INF, INF],  # B
    [INF, INF, 0, INF, INF],  # C
    [INF, INF, 32, 0, INF],  # D
    [7, INF, INF, INF, 0]  # E
]

# Graf jako lista sąsiedztwa
graph_adj_list = {
    'A': [('B', 10), ('C', 12), ('D', 60)],
    'B': [('C', 20)],
    'C': [],
    'D': [('C', 32)],
    'E': [('A', 7)]
}

# Graf jako słownik sąsiedztwa
graph_dict = {
    'A': {'B': 10, 'C': 12, 'D': 60},
    'B': {'C': 20},
    'C': {},
    'D': {'C': 32},
    'E': {'A': 7}
}

# Graf jako lista krawędzi
graph_edges = [
    ('A', 'B', 10),
    ('A', 'C', 12),
    ('A', 'D', 60),
    ('B', 'C', 20),
    ('D', 'C', 32),
    ('E', 'A', 7)
]


graph_For_BFS_DFS = {
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


def dijkstra(g, n, start):
    dist = [float('inf') for _ in range(1, n + 1)]
    dist[start - 1] = 0
    queue = [i for i in range(1, n + 1)]
    while queue:

        min1 = float('inf')
        for i in queue:
            if dist[i - 1] < min1:
                min1 = i
        node = min1

        try:
            queue.remove(min1)
        except:
            return dist

        for neighbour in g[node]:
            if dist[neighbour[0] - 1] > dist[node - 1] + neighbour[1]:
                dist[neighbour[0] - 1] = dist[node - 1] + neighbour[1]
    return dist


def bellmanFord(g, n, start):
    dist = [float('inf') for _ in range(1, n + 1)]
    dist[start - 1] = 0

    for _ in range(n - 1):
        for neighbour in g:
            for v, weight in g[neighbour]:                          # silly
                if dist[neighbour - 1] + weight < dist[v - 1]:
                    dist[v - 1] = dist[neighbour - 1] + weight

    # brakuje sprawdzenia nieskonczonych wezlow jeszce
    return dist


