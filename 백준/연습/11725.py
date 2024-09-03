import sys
sys.setrecursionlimit(10**5)

def dfs(graph, x, visited):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            parents[i] = x
            dfs(graph, i, visited)
     

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) 
parents = [1] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)

for i in range(2, N+1):
    print(parents[i])