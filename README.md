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

## Water Jug Problem

START
1. Initialize jug capacities A = 8, B = 5, C = 3.
2. Set initial state as (8, 0, 0).
3. Set the target state as (4, 4, 0).
4. Insert the initial state into the queue.
5. WHILE the queue is not empty:
      a. Remove a state from the queue.
      b. IF the state equals the target:
            PRINT the solution.
            STOP.
      c. Generate new states by pouring water
         between jugs.
      d. Add unvisited states to the queue.
6. PRINT "No solution found".
STOP

## A* Search Algorithm

BEGIN
1. Add the start node to OPEN.
2. WHILE OPEN is not empty:
   a. Select node with lowest f(n).
   b. If node is the goal, return path.
   c. Move node to CLOSED.
   d. For each neighbour:
      Calculate g(n).
      Calculate f(n) = g(n) + h(n).
      Update cost and parent if better.
      Add neighbour to OPEN if needed.
3. Return failure.
END

## Greedy Best-First Search (GBFS)

BEGIN
1. Add the start node to OPEN.
2. WHILE OPEN is not empty:
   a. Select node with lowest h(n).
   b. If node is the goal, return path.
   c. Move node to CLOSED.
   d. Add unexplored neighbours to OPEN.
      Store their heuristic values and parents.
3. Return failure.
END

## Mini-max Algorithm

BEGIN
1. If node is terminal, return its value.
2. If node is MAX:
      best = -INFINITY
      For each child:
          best = MAX(best, MINIMAX(child))
      Return best.
3. Otherwise, node is MIN:
      best = +INFINITY
      For each child:
          best = MIN(best, MINIMAX(child))
      Return best.
END

## Alpha-Beta Pruning

BEGIN
1. If node is terminal, return its value.
2. If node is MAX:
      best = -INFINITY
      For each child:
          best = MAX(best, ALPHA_BETA(child))
          alpha = MAX(alpha, best)
          If alpha >= beta, BREAK.
      Return best.
3. Otherwise, node is MIN:
      best = +INFINITY
      For each child:
          best = MIN(best, ALPHA_BETA(child))
          beta = MIN(beta, best)
          If alpha >= beta, BREAK.
      Return best.
END

## N-Queens Problem

BEGIN
1. Start with an empty chessboard.
2. Place one queen in each row.
3. For each column:
      Check whether the position is safe.
      If safe:
          Place the queen.
          Recursively solve the next row.
          If unsuccessful, remove the queen.
4. If all rows are filled, return SUCCESS.
5. Otherwise, return FAILURE.
END

## Map Colouring using CSP

BEGIN
1. Define regions, neighbours, and available colours.
2. Select an uncoloured region.
3. For each available colour:
      Check whether neighbouring regions
      have the same colour.
      If no conflict:
          Assign the colour.
          Recursively colour the remaining regions.
          If unsuccessful, remove the colour.
4. If all regions are coloured, return SUCCESS.
5. Otherwise, return FAILURE.
END
