from collections import deque
import sys

def bfs(z, y, x):
    while queue:
        z, y, x = queue.popleft()
        for k in range(6):
            nz, ny, nx = z + dz[k] , y + dy[k], x + dx[k] #위아래상하좌우
            if ny >= N or ny < 0 or nx >= M or nx < 0 or nz >= H or nz < 0 :
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append([nz ,ny, nx])

M, N, H = map(int, input().split()) # M은 가로 칸 수, N은 세로 칸 수, H는 높이
graph = []
queue = deque()
max_value = 0
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
    graph.append(layer)
    
for k in range(H):    
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1 :
                queue.append([k, i, j])

bfs(0, 0, 0)

for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0:
                print(-1)
                sys.exit()
            if graph[k][i][j] > max_value:
                max_value = graph[k][i][j]

print(max_value - 1)

# 3차원 배열써서 상하를 dz로 둬서 추가해주기