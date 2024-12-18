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