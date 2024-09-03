from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, land):
    queue = deque([[y,x]])
    visited[y][x] = True
    land[y][x] = point
    oil = 1
    y_max, x_max = len(visited), len(visited[0])
    while queue:
        ky, kx = queue.popleft()
        for k in range(4):
            ny, nx = ky + dy[k], kx + dx[k]
            
            if ny >= y_max or nx >= x_max or nx < 0 or ny < 0:
                continue
            
            if visited[ny][nx] == False and land[ny][nx] != 0:
                visited[ny][nx] = True
                land[ny][nx] = point
                oil += 1
                queue.append([ny, nx])
    
    oils[point] = oil
                
        
def solution(land):
    global y_max, x_max, max_arr, visited, oils, point
    y_max, x_max = len(land), len(land[0])
    max_arr = []
    point = 1
    visited = [[0] * x_max for _ in range(y_max)]
    oils = {}
    
    for i in range(x_max): # x축
        for j in range(y_max): # y축
            if land[j][i] != 0 and visited[j][i] == False:
                bfs(j, i, land)
                point += 1
    
    for k in range(x_max):
        sets = set()
        total = 0
        for i in range(y_max):
            if land[i][k] != 0:
                sets.add(land[i][k])
        
        for ans in sets:
            total += oils[ans]
        max_arr.append(total)
    
    return max(max_arr)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))

# 처음엔 매 열마다 Visited 배열을 선언하여서 누적값을 더하려고 했으나 그렇게 하니 효율성에서 시간 초과 발생
# 그래서 기름 체취 구역을 point로 정하고 이후 탐색을 통해 set에 저장
# 딕셔너리 키 값을 통해 누적값 구함.