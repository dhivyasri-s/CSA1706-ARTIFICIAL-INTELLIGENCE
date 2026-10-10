## 1
from collections import deque

def water_jug():
    capacity1 = 5
    capacity2 = 3
    target = 4

    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parent = {}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            state = (a, b)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            path.reverse()

            for step in path:
                print("5L jug:", step[0], "| 3L jug:", step[1])
            return

        states = [
            (5, b),
            (a, 3),
            (0, b),
            (a, 0),
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            (a + min(b, 5 - a), b - min(b, 5 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)

water_jug()

## 2
from collections import deque

def water_jug():
    capacities = (12, 8, 5)
    start = (12, 0, 0)
    target = 6

    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()

        if state[1] == target:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            for step in path:
                print("12L:", step[0],
                      "8L:", step[1],
                      "5L:", step[2])
            return

        for i in range(3):
            for j in range(3):
                if i == j:
                    continue

                amount = min(
                    state[i],
                    capacities[j] - state[j]
                )

                if amount == 0:
                    continue

                new_state = list(state)
                new_state[i] -= amount
                new_state[j] += amount
                new_state = tuple(new_state)

                if new_state not in parent:
                    parent[new_state] = state
                    queue.append(new_state)

    print("Target cannot be reached")

water_jug()

## 3
from collections import deque

capacity = (12, 8, 5)
start = (12, 0, 0)
target = (6, 6, 0)

queue = deque([start])
parent = {start: None}
found = False

while queue:
    state = queue.popleft()

    if state == target:
        found = True
        path = []

        while state is not None:
            path.append(state)
            state = parent[state]

        path.reverse()

        print("12L  8L  5L")
        for a, b, c in path:
            print(a, "  ", b, "  ", c)
        break

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            amount = min(state[i], capacity[j] - state[j])

            if amount > 0:
                new_state = list(state)
                new_state[i] -= amount
                new_state[j] += amount
                new_state = tuple(new_state)

                if new_state not in parent:
                    parent[new_state] = state
                    queue.append(new_state)

if not found:
    print("Target not possible")

## 4
from collections import deque

def water_jug():
    capacity = (8, 5, 3)
    start = (8, 0, 0)
    target = (4, 4, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == target:
            print("Solution:")
            for step in path:
                print(step)
            return

        for i in range(3):
            for j in range(3):
                if i != j:
                    new_state = list(state)
                    amount = min(state[i], capacity[j] - state[j])

                    new_state[i] -= amount
                    new_state[j] += amount
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))

    print("No solution found")

water_jug()    
