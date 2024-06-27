from collections import deque
def solution(n, computers):
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False :
                bfs(n, computers, i, j)
                return networks
    answer = networks
    return answer

def bfs(n, computers, y, x):
    global networks
    queue.append([y,x])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for k in range(n):
            nx = k
            if nx < n and y < n and nx >= 0 and y >= 0 :
                if computers[y][nx] == 1 and visited[y][nx] == False:
                    visited[y][nx] = True
                    queue.append([nx, y])
    networks += 1
    for i in range(n):
        visited[i][i] = True
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False:
                bfs(n, computers, i, j)
    
    return networks
                    
queue = deque()
networks = 0
visited = [[False] * (201) for _ in range(201)]
dx = [1] * 201

        

print(solution(3, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# bfs로 푸는데 nx에 x + dx 줬다가 계속 1만 들어가길래 k를 더해서 모든 x 순차적으로 확인하게 했음. 1번이 2번이랑 연결되어 있으면 2번에 대한 정보를 y, x 값 반대로 q에 넣어서 다시 순찰