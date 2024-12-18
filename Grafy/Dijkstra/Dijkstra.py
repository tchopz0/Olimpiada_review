graph_for_Dijkstra = {
    1: [(2, 2), (3, 4)],
    2: [(4, 7)],
    3: [(4, 1), (5, 3)],
    4: [(6, 1)],
    5: [(4, 2), (6, 5)],
    6: []
}


def dijkstra(graph, start):
    dist = [float('inf') for _ in range(1, len(graph) + 1)]
    dist[start - 1] = 0
    queue = [i for i in range(1, len(graph) + 1)]
    print(dist, queue)
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

        for neighbour in graph[node]:
            if dist[neighbour[0] - 1] > dist[node - 1] + neighbour[1]:
                dist[neighbour[0] - 1] = dist[node - 1] + neighbour[1]
    return dist


print(dijkstra(graph_for_Dijkstra, 1))
