V, L, R = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(R):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

print(graph)