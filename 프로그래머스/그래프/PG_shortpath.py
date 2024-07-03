from collections import deque

def solution(maps):
    answer = bfs(len(maps), len(maps[0]), maps, 0, 0)
    return answer

def bfs(N, M, maps, y, x):
    queue.append([y,x])
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if ny >= N or ny < 0 or nx >= M or nx < 0:
                continue
            if maps[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])
    if visited[N-1][M-1] == 0:
        return -1
    
    return visited[N-1][M-1] + 1
        
queue = deque()
visited = [[0] * (101) for _ in range(101)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))