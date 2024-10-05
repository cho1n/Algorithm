from collections import deque

def bfs(N, K):
    queue = deque([(N, 1)])
    while queue:
        current, steps = queue.popleft()
        
        if current == K:
            return steps
        
        if current * 2 <= K:
            queue.append((current * 2, steps + 1))
        
        if int(str(current) + '1') <= K:
            queue.append((int(str(current) + '1'), steps + 1))
    
    return -1

N, K = map(int, input().split())
print(bfs(N, K))
