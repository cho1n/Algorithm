from collections import deque

def bfs(y, x, color):
    queue.append([y, x])
    
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if ny >= N or nx >= N or ny < 0 or nx < 0:
                continue
            
            if visited[ny][nx] == False:
               if graph[ny][nx] == color:
                   visited[ny][nx] = True
                   queue.append([ny, nx])

N = int(input())
graph = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
per1, per2 = 0, 0
queue = deque()

for l in range(N):
    graph.append(list(map(str, input())))

visited = [[False] * N for _ in range(N)]
# R, G, B
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, graph[i][j])
            per1 += 1
            
visited = [[False] * N for _ in range(N)]

#RG
for l in range(N):
    for k in range(N):
        if graph[l][k] == 'G':
            graph[l][k] = 'R'

for a in range(N):
    for b in range(N):
        if visited[a][b] == False:
            bfs(a, b, graph[a][b])
            per2 += 1

print(per1, per2)