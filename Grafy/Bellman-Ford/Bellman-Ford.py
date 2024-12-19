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

    # brakuje sprawdzenia nieskonczonych wezlow jeszce
    return dist

print(bellmanFord(graph_for_Bellman_Ford, 1))