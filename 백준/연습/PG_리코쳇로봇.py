from collections import deque


    

def solution(board):
    answer = 0
        
    
    def bfs(y, x):
        global answer
        while queue:
            y, x = queue.popleft()
            visited[y][x] = True
            nx, ny = x, y
        
            while True:
                for k in range(4):
                    nx, ny = nx + dx[k], ny + dy[k]
                    
                if ny >= len(board) or nx >= len(board[0]) or nx < 0 or ny < 0:
                    break
                if board[ny][nx] == 'D':
                    break
            
            if visited[ny - dy[k]][nx - dx[k]] == -1:
                visited[ny - dy[k]][nx - dx[k]] = visited[y][x] + 1
                queue.append([ny - dy[k], nx - dx[k]])
                        

    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append([i,j])
                bfs(i, j)
            elif board[i][j] == 'G':
                y_goal, x_goal = i, j
                
    
    answer = visited[y_goal][x_goal]
    
    return answer

dy = [-1, 1, 0, 0] # 상하
dx = [0, 0, -1, 1] # 좌우
queue = deque()

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
