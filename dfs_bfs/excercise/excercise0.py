graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# dfs
def dfs0(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs0(graph, i, visited)

#dfs0(graph, 1, visited)

# bfs
from collections import deque

def bfs0(graph, v, visited):
    
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs0(graph, 1, visited)