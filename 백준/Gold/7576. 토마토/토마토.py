from collections import deque
import sys

def bfs(y, x):
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k] #상하좌우  
            if ny >= N or ny < 0 or nx >= M or nx < 0 :
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])
            

M, N = map(int, input().split()) # M은 가로 칸 수, N은 세로 칸 수
graph = []
queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split(' '))))
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 :
            queue.append([i, j])

bfs(0, 0)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()

print(max(map(max, graph)) - 1)