## 1

import math

def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        best = -math.inf

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = math.inf

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


# Game tree from the diagram
tree = [
    [
        [2, 3],   # D
        [5, 9]    # E
    ],
    [
        [6, 1],   # F
        [7, 5]    # G
    ]
]

result = alpha_beta(tree, 3, -math.inf, math.inf, True)

print("Optimal Value:", result)
