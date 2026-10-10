from collections import deque

graph = {
    1: [3, 6],
    3: [4, 8, 1],
    4: [3, 7],
    7: [4, 8],
    8: [7, 3],
    6: [1, 9, 5],
    9: [6],
    5: [6]
}

visited = []
queue = deque([1])

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

print("BFS Traversal:", visited)
