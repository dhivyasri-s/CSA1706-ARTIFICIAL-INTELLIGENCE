from collections import deque
graph={
    1:[2,3],
    2:[4,5],
    3:[],
    4:[5],
    5:[]


}
def bfs(start):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            print("BFS traversal:",visited)
bfs(1)
