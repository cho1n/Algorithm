from collections import deque
from itertools import combinations

def bfs(y, x, new_graphs):
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if 0 > nx or 0 > ny or ny >= N or nx >= M:
                continue
            
            if new_graphs[ny][nx] == 0:
                if new_graphs[y][x] == 2:
                    new_graphs[ny][nx] = 2
                    queue.append([ny, nx])

N, M = map(int, input().split())
graph = []
queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
max = 0
empty = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append([i,j])
            
possible_wall = combinations(empty, 3)

for wall in possible_wall:
    new_graph = [row[:] for row in graph]
    count = 0
    
    for y, x in wall:
        new_graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                bfs(i, j, new_graph)
    
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 0:
                count += 1
    
    if count > max:
        max = count
            
print(max)