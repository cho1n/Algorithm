import heapq

INF = 1e8
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(K)

print(graph)

for i in range(1, V+1):
    if distance[i] == 1e8:
        print("INF")
    else:
        print(distance[i])
    