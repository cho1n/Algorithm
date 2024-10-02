N = int(input())
Find_N = int(input())

graph = [[0] * N for _ in range(N)]

graph[0][0] = N*N
answer_y, answer_x = 0, 0

y, x = 0, 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
direction = 0

while graph[N//2][N//2] != 1:
    ny = y + dy[direction]
    nx = x + dx[direction]
            
    if ny >= N or nx >= N or ny < 0 or nx < 0 or graph[ny][nx] != 0:
        direction = (direction + 1) % 4
        continue
        
    if graph[ny][nx] == 0:
        graph[ny][nx] = graph[y][x] - 1
        y, ny = ny, y
        x, nx = nx, x            
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == Find_N:
            answer_y, answer_x = i, j
            break

for row in graph:
    print(' '.join(map(str, row)))
print(answer_y+1, answer_x+1)

