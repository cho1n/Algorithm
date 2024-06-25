from collections import deque
import sys

N, K = map(int, input().split())

if N == K:
    print(0)
    sys.exit()

graph = [1] * 100001
dx = [-1, 1, 2]

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
                print(graph[x])
                sys.exit()
            if 0 <= nx < 100001:
                if graph[nx] == 1:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)

print(bfs(N))