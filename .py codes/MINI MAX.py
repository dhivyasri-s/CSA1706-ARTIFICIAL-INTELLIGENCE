## 1

def minimax(node, depth, maximizing):
    if isinstance(node, int):
        return node

    if maximizing:
        best = float('-inf')
        for child in node:
            value = minimax(child, depth + 1, False)
            best = max(best, value)
        return best
    else:
        best = float('inf')
        for child in node:
            value = minimax(child, depth + 1, True)
            best = min(best, value)
        return best


# Game tree from the diagram
tree = [
    [
        [2, 3],
        [5, 9]
    ],
    [
        [0, 1],
        [4, 5]
    ]
]

# A is MAX
result = minimax(tree, 0, True)

print("Optimal value:", result)
