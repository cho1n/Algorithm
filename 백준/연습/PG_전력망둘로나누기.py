from collections import deque

def bfs(graph, v, visited):
    n = 1
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    n += 1
    return n
    

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = []
    rem = 0
    
    for i in range(n-1):
        u, v = wires[i][0], wires[i][1]
        graph[u].append(v)
        graph[v].append(u)
        
    for j in range(1, n):
        for k in range(len(graph[j])):
            visited = [False] * (n+1)
            rem = graph[j][k]
            graph[j][k] = None
            
            n1 = bfs(graph, 1, visited)
            n2 = bfs(graph, n, visited)
            
            answer.append(abs(n1 - n2))
            graph[j][k] = rem
            
    print(graph)
    print(answer)
    return min(answer)

print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))