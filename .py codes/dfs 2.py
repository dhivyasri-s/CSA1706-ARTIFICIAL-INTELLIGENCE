graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

visited = []

def dfs(node):
    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(1)

print("DFS Traversal:", visited)
