from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
            
        
T = int(input())
for Z in range(T):
    M, N, K = map(int, input().split()) # M:가로 N:세로 K:배추갯수
    result = 0
    graph = [[0 for j in range(N)] for i in range(M)]
    
    for _ in range(K) :
        u, v = map(int, input().split())
        graph[u][v] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i,j)
                result += 1

    print(result)