from collections import deque

board = [0] * (101)
visited = [0] * (101)
ladder = [0] * (101)
snake = [0] * (101)

dx = [1, 2, 3, 4, 5, 6]
N, M = map(int, input().split())

for i in range(N):
    x, y = map(int, input().split())
    if y > x :
        ladder[x] = y

for i in range(M):
    u, v = map(int, input().split())
    if u > v :
        snake[u] = v

def dfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for k in range(6):
            nx = x + dx[k]
            if nx > 100 or nx < 0 :
                continue
            if board[nx] == 0 and visited[nx] == False:
                visited[nx] = True
                if ladder[nx] != 0 :
                    ny = ladder[nx]
                    if visited[ny] == False: 
                        visited[ny] = True
                        board[nx] = board[x] + 1
                        board[ny] = board[x] + 1
                        queue.append(ny)
                elif snake[nx] != 0 :
                    ny = snake[nx]
                    if visited[ny] == False: 
                        visited[ny] = True
                        board[nx] = board[x] + 1
                        board[ny] = board[x] + 1
                        queue.append(ny)       
                else:
                    board[nx] = board[x] + 1
                    queue.append(nx)
    return board[100]

print(dfs(1))