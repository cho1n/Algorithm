from collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        
N, M, V = map(int, input().split()) 

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) 

for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, V, visited)
visited = [False] * (N+1)
print()
bfs(graph, V, visited)


