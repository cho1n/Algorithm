import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1 and visited[nx][ny] == False :
                visited[nx][ny] = True
                dfs(nx, ny)
        
T = int(input())
for Z in range(T):
    M, N, K = map(int, input().split()) # M:가로 N:세로 K:배추갯수
    result = 0
    graph = [[0 for j in range(N)] for i in range(M)]
    visited = [[False for j in range(N)] for i in range(M)]

    for _ in range(K) :
        u, v = map(int, input().split())
        graph[u][v] = 1
        
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                result += 1
                dfs(i, j)

    print(result)