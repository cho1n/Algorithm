from collections import deque
import sys

N, K = map(int, input().split())

if N == K:
    print(0)
    sys.exit()

graph = [0] * 100001
visited = [False] * 100001
dx = [2, -1, 1]

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        visited[x] = True
        for k in range(3) :
            if k == 0 :
                nx = x * dx[k]
            else :
                nx = x + dx[k]   
                
            if nx == K and ( k == 1 or k == 2 ):
                print(graph[x] + 1)
                sys.exit()
            elif nx == K and k == 0:
                print(graph[x])
                sys.exit()
                
            if 0 <= nx < 100001 and visited[nx] == False:
                if graph[nx] == 0:
                    if nx == x * dx[k]:
                        graph[nx] = graph[x]
                        queue.appendleft(nx)
                    else:
                        graph[nx] = graph[x] + 1
                        queue.append(nx)
                    visited[nx] = True
print(bfs(N))

# 4 6 -> 4 3 6 1초 , 4 5 6 2초
# 방문처리가 중요한 게 아니라 역대 최단거리를 갱신하는 메커니즘이 중요
# 다음 번에 한 번 더 풀어볼 것