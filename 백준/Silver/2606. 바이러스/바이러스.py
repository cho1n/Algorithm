def dfs(graph, v, visited, order, count) :
    visited[v] = True
    order[v] = count[0]
    count[0] += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, order, count)


N = int(input())
K = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) 
order = [0] * (N+1)
count = [1]

for _ in range(K) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited, order, count)

print(max(order) - 1)