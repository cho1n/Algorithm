from collections import deque
import sys

N, K = map(int, input().split())

graph = [0] * 100001
dx = [-1, 1, 2]

if N == K:
    print(graph[N])
    sys.exit()

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for k in range(3) :
            if k == 2 :
                nx = x * dx[k]
            else :
                nx = x + dx[k]   
                
            if nx == K:
                print(graph[x] + 1)
                sys.exit()
                
            if 0 <= nx < 100001:
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
                

print(bfs(N))