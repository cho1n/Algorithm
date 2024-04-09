import sys
from collections import deque

N = int(input())
K = int(input())
result = 0
graph = [[] for _ in range(N + 1)]
visited = [0] * (N+1)

for m in range(K):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

bfs(graph, 1, visited)
print(sum(visited)-1)        
