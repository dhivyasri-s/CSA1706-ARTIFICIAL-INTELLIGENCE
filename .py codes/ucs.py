##1

graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}
}

distance = {
    'S': 0, 'A': float('inf'), 'B': float('inf'),
    'C': float('inf'), 'D': float('inf'), 'G': float('inf')
}

previous = {}
unvisited = list(graph.keys())

while unvisited:
    current = min(unvisited, key=lambda node: distance[node])

    if distance[current] == float('inf'):
        break

    unvisited.remove(current)

    for neighbour, weight in graph[current].items():
        new_distance = distance[current] + weight

        if new_distance < distance[neighbour]:
            distance[neighbour] = new_distance
            previous[neighbour] = current

path = []
node = 'G'

while node in previous:
    path.append(node)
    node = previous[node]

path.append('S')
path.reverse()

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", distance['G'])

##2

graph = {
    'V1': {'V2': 9, 'V3': 4},
    'V2': {'V1': 9, 'V3': 2, 'V4': 7, 'V5': 3},
    'V3': {'V1': 4, 'V2': 2, 'V4': 3, 'V5': 6},
    'V4': {'V2': 7, 'V3': 3, 'V5': 4, 'V6': 8},
    'V5': {'V2': 3, 'V3': 6, 'V4': 4, 'V6': 2},
    'V6': {'V4': 8, 'V5': 2}
}

distance = {node: float('inf') for node in graph}
previous = {}
distance['V1'] = 0
unvisited = list(graph.keys())

while unvisited:
    current = min(unvisited, key=lambda node: distance[node])
    unvisited.remove(current)

    if distance[current] == float('inf'):
        break

    for neighbour, weight in graph[current].items():
        new_distance = distance[current] + weight

        if new_distance < distance[neighbour]:
            distance[neighbour] = new_distance
            previous[neighbour] = current

path = []
node = 'V6'

while node in previous:
    path.append(node)
    node = previous[node]

path.append('V1')
path.reverse()

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", distance['V6'])
