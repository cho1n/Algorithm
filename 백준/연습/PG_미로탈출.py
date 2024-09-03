from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(maps):
    visited_laver = [[-1] * len(maps[0]) for _ in range(len(maps))]
    visited_exit = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    x_max, y_max = len(maps[0]), len(maps)
    goal = [0, 0]
    answer = 0
    flag = [0]
    
    def bfs_laver(y, x):
        while q:
            y, x = q.popleft()
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                
                if nx >= x_max or ny >= y_max or ny < 0 or nx < 0:
                    continue
                
                if visited_laver[ny][nx] == -1:
                    if maps[ny][nx] == 'O':
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        q.append([ny,nx])
                    elif maps[ny][nx] == 'L':
                        flag[0] = 1 
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        return ny, nx  # 라바에 도착하면 좌표 반환
                    elif maps[ny][nx] == 'E':
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        if flag[0] == 0:
                            q.append([ny, nx])
                        else:
                            return ny, nx  # 탈출구에 도착하면 좌표 반환
        return -1, -1
        
    def bfs_exit(y, x):
        q.clear()
        q.append([y, x])
        visited_exit[y][x] = True
        
        while q:
            y, x = q.popleft()
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                    
                if nx >= x_max or ny >= y_max or ny < 0 or nx < 0:
                    continue
                    
                if not visited_exit[ny][nx]:
                    if maps[ny][nx] == 'O':
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        visited_exit[ny][nx] = True
                        q.append([ny,nx])
                    elif maps[ny][nx] == 'S':
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        visited_exit[ny][nx] = True
                        q.append([ny, nx])
                    elif maps[ny][nx] == 'E':
                        visited_laver[ny][nx] = visited_laver[y][x] + 1
                        return ny, nx  # 탈출구에 도착하면 좌표 반환

        return -1, -1

    for i in range(y_max):
        for j in range(x_max):
            if maps[i][j] == 'S':
                q.append([i, j])
                visited_laver[i][j] = 0
                goal[0], goal[1] = bfs_laver(i, j)
                
    if maps[goal[0]][goal[1]] == 'L' and flag[0] == 1:
        q.append([goal[0], goal[1]])
        visited_exit[goal[0]][goal[1]] = True
        goal[0], goal[1] = bfs_exit(goal[0], goal[1])
    
    print(visited_laver)
    
    if flag[0] == 1 and goal[0] != -1 and goal[1] != -1 :
        answer = visited_laver[goal[0]][goal[1]]
    else:
        answer = -1
    return answer

print(solution(["LOSOE"]))
