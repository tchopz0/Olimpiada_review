graphForDfs = {
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


def dfs_iteratively(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            # space for node processing, e.g. print
            # print(node)
            visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)


def dfs_recursively(graph, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    # space for node processing, e.g. print
    print("node: " + str(node))
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursively(graph, neighbour, visited)



dfs_iteratively(graphForDfs, 'A')


# node - start
# visited = None - the function can be called without declaring it
dfs_recursively(graphForDfs, 'A')


