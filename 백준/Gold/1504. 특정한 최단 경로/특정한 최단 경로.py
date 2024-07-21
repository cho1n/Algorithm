import heapq

INF = 987654321
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N+1)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
    return distance[end]
    
start, end = map(int, input().split())
if start <= N and end <= N :
    path1 = dijkstra(1, start) + dijkstra(start, end) + dijkstra(end, N)
    path2 = dijkstra(1, end) + dijkstra(end, start) + dijkstra(start, N)
    ans = min(path1, path2)
    if ans >= INF :
        print(-1)
    else:
        print(ans)
else:
    print(-1)