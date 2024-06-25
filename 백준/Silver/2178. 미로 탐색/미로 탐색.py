from collections import deque

N, M = map(int, input().split()) # N은 열 M은 행

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):    
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if N <= nx or 0 > nx or 0 > ny or ny >= M :
                continue 
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[N-1][M-1]
        
print(bfs(0,0))