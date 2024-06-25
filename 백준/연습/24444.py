from collections import deque

def bfs(graph, v, visited, order, counter):
    queue = deque([v])
    visited[v] = True
    order[v] = counter[0]
    counter[0] += 1
    print(queue)
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                order[i] = counter[0]
                counter[0] += 1


V, E, R = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
order = [0] * (V + 1)
counter = [1]

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, R, visited, order, counter)

for i in range(1, V + 1):
    print(order[i])