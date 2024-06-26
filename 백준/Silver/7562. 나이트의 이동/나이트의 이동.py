from collections import deque
import sys

def bfs(y, x):
    queue = deque()
    queue.append([y,x])
    
    while queue:
        y, x = queue.popleft()
        for k in range(8):
            ny, nx = y + dy[k], x + dx[k]
             
            if 0 > ny or ny >= I or nx >= I or nx < 0 :
                continue
            if ny == endY and nx == endX :
                return(graph[y][x] + 1)
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
startY, startX, endY, endX = 0, 0, 0, 0
T = int(input())
for Z in range(T):
    I = int(input()) # I = 정사각형 한 변의 길이
    graph = [[0 for j in range(I)] for i in range(I)]
    chess = [[False for j in range(I)] for i in range(I)]
    
    startY, startX = map(int, input().split())    
    endY, endX = map(int, input().split())
    
    if startX == endX and startY == endY :
        print(0)
        continue
    
    print(bfs(startY, startX))