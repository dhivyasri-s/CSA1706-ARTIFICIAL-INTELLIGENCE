##1
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    print("BFS Traversal:", visited)

bfs(1)

##2
from collections import deque

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

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

    print("BFS Traversal:", end=" ")
    print(*visited)

bfs(1)

##3
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

##4
from collections import deque

graph = {
    0: [1],
    1: [3],
    2: [1],
    3: [2, 4],
    4: [5],
    5: [7],
    6: [4],
    7: [6]
}

visited = []
queue = deque([0])

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

print("BFS Traversal:", visited)
