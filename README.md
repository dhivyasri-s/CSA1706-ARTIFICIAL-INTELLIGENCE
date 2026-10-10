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
