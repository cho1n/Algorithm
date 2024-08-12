from collections import deque

def bfs(y, x):
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for k in range(8):
            ny, nx = y + dy[k], x + dx[k]
            if ny >= h or ny < 0 or nx >= w or nx < 0:
                continue
            if graph[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append([ny, nx])
            

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    queue = deque()
    graph = []
    visited = [[False] * w for _ in range(h)]
    count = 0
    
    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        graph.append(list(map(int, input().split(' '))))
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                queue.append((i, j))
                bfs(i, j)
                count += 1
    print(count)