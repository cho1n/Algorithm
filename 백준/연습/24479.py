import sys
sys.setrecursionlimit(10**5)

def dfs(graph, v, visited, order, counter):
    visited[v] = True
    order[v] = counter[0]
    counter[0] += 1
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited, order, counter)

V, E, R = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
order = [0] * (V + 1)
counter = [1]

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, R, visited, order, counter)

for i in range(1, V + 1):
    print(order[i])
