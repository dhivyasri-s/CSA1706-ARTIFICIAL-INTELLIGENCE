## BFS (Breadth-First Search)

START
1. Initialize VISITED as an empty list.
2. Initialize an empty QUEUE.
3. Insert the starting node into QUEUE.

4. WHILE QUEUE is not empty:
      a. Remove the first node from QUEUE.
      b. IF node is not in VISITED:
            i. Add node to VISITED.
           ii. FOR each neighbour of node:
                   IF neighbour is not in VISITED:
                       Insert neighbour into QUEUE.

5. Display VISITED.
STOP

## DFS (Depth-First Search)

START
1. Initialize VISITED as an empty list.

2. Define DFS(node):
      a. IF node is not in VISITED:
             i. Add node to VISITED.
            ii. FOR each neighbour of node:
                    CALL DFS(neighbour).

3. CALL DFS(starting node).
4. Display VISITED.
STOP

## UCS (Uniform Cost Search)

START

1. Initialize an empty PRIORITY QUEUE.
2. Insert the starting node with cost 0.
3. Initialize VISITED as an empty set.

4. WHILE PRIORITY QUEUE is not empty:

      a. Remove the node with the lowest cost.

      b. IF the node is the goal node:
             Display the path and total cost.
             STOP.

      c. IF the node is not in VISITED:
             Add the node to VISITED.

      d. FOR each neighbour of the current node:
             Calculate new cost =
                 current cost + edge cost.

5. If the goal is not found:
      Display "Path not found".

STOP
