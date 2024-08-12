from collections import deque

def bfs(y, x, height):
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k] 
            if ny >= N or ny < 0 or nx >= N or nx < 0 :
                continue
            if graph[ny][nx] > height and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append([ny, nx])            

N = int(input())
graph = []
queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
max_value = 0

for i in range(N):
    graph.append(list(map(int, input().split(' '))))
    
a = max(map(max, graph))

for i in range(a):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if visited[j][k] == False and graph[j][k] > i:
                queue.append((j,k))
                bfs(j, k, i)
                count += 1
    if count > max_value:
        max_value = count

print(max_value)