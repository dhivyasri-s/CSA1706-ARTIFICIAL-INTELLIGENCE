##1
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            dfs(neighbour)

print("DFS Traversal:", end=" ")
dfs(1)

##2
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
    if node not in visited:
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

print("DFS Traversal:", end=" ")
dfs(1)
print(*visited)

##3
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

def dfs(node):
    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(1)

print("DFS Traversal:", visited)

##4
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

def dfs(node):
    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(0)

print("DFS Traversal:", visited)
