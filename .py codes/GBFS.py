## 1

import heapq

# Graph (connections between nodes)
graph = {
    'A': ['D', 'C', 'B'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['A', 'F'],
    'E': ['B', 'C', 'H'],
    'F': ['D', 'C', 'G'],
    'H': ['E', 'G'],
    'G': ['F', 'H']
}

# Heuristic values h(n)
h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

def gbfs(start, goal):
    priority_queue = [(h[start], start, [start])]
    visited = set()

    while priority_queue:
        heuristic, node, path = heapq.heappop(priority_queue)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Nodes Visited:", len(visited) + 1)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (h[neighbor], neighbor, path + [neighbor])
                )

    print("Goal not found")


# Execute GBFS
gbfs('A', 'G')

## 2

import heapq

# Directed graph with edge costs
graph = {
    'P': {'R': 4, 'C': 4, 'A': 4},
    'C': {'R': 2, 'M': 6, 'U': 3},
    'R': {'E': 5},
    'E': {'S': 1, 'U': 5},
    'A': {'M': 3},
    'M': {'U': 0, 'L': 2},
    'U': {'S': 4, 'N': 5},
    'L': {'N': 5},
    'N': {'S': 6},
    'S': {}
}

# Heuristic values h(n)
h = {
    'P': 10,
    'R': 8,
    'C': 6,
    'A': 11,
    'M': 9,
    'U': 4,
    'L': 9,
    'E': 3,
    'N': 6,
    'S': 0
}

def a_star(start, goal):
    pq = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if g > best_cost.get(node, float('inf')):
            continue

        for neighbor, cost in graph[node].items():
            new_g = g + cost

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                new_f = new_g + h[neighbor]
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    print("Goal not found")


# Start node P, goal node S
a_star('P', 'S')
