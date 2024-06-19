import sys
from collections import deque

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
DFS_visited = [False] * (N+1)
BFS_visited = [False] * (N+1)

for m in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort()
    
def bfs(graph, start, visited): 
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                                
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, start, DFS_visited)
print()
bfs(graph, start, BFS_visited)
