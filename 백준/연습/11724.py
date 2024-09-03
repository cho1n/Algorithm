from collections import deque

count = 0

def bfs(graph, v, visited):
    global count
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    count += 1

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) 

for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if visited[i] == False:
        bfs(graph, i, visited)

if M == 0:
    print(N)
else:
    print(count)