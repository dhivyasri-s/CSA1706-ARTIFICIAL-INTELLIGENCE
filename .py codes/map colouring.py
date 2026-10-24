## 1

# Map Colouring Problem using CSP

colors = ["Red", "Green", "Blue"]

graph = {
    "Germany": ["Poland", "Czech", "Austria", "Switzerland"],
    "Poland": ["Germany", "Czech", "Slovakia"],
    "Czech": ["Germany", "Poland", "Slovakia", "Austria"],
    "Slovakia": ["Poland", "Czech", "Austria", "Hungary"],
    "Austria": ["Germany", "Czech", "Slovakia", "Hungary", "Italy", "Switzerland"],
    "Switzerland": ["Germany", "Austria", "Italy"],
    "Italy": ["Austria", "Switzerland"],
    "Hungary": ["Austria", "Slovakia"]
}

assignment = {}


def is_safe(country, color):
    for neighbor in graph[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve():
    if len(assignment) == len(graph):
        return True

    country = next(country for country in graph if country not in assignment)

    for color in colors:
        if is_safe(country, color):
            assignment[country] = color

            if solve():
                return True

            del assignment[country]

    return False


if solve():
    print("Map Colouring Solution:")
    for country, color in assignment.items():
        print(country, ":", color)
else:
    print("No solution exists.")

## 2

# Map Colouring Problem using CSP and Backtracking

colors = ["Red", "Green", "Blue"]

graph = {
    "Germany": ["Poland", "Czech", "Austria", "Switzerland"],
    "Poland": ["Germany", "Czech", "Slovakia"],
    "Slovakia": ["Poland", "Czech", "Hungary", "Austria"],
    "Czech": ["Germany", "Poland", "Slovakia", "Austria"],
    "Austria": ["Germany", "Czech", "Slovakia", "Hungary", "Italy", "Switzerland"],
    "Switzerland": ["Germany", "Austria", "Italy"],
    "Italy": ["Switzerland", "Austria"],
    "Hungary": ["Austria", "Slovakia"]
}

assignment = {}


def is_safe(country, color):
    for neighbor in graph[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve():
    if len(assignment) == len(graph):
        return True

    country = next(c for c in graph if c not in assignment)

    for color in colors:
        if is_safe(country, color):
            assignment[country] = color

            if solve():
                return True

            del assignment[country]

    return False


if solve():
    print("Map Colouring Solution:")
    for country, color in assignment.items():
        print(country, ":", color)
else:
    print("No solution exists.")
    
