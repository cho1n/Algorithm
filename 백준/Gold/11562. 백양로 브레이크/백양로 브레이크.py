n, m = map(int, input().split())
INF = 987654321
costs = [[INF] * n for _ in range(n)]

for i in range(m):
    start, end, way = map(int, input().split())
    if way == 0:
        costs[start-1][end-1] = 0   
        costs[end-1][start-1] = 1
    elif way == 1:
        costs[start-1][end-1] = 0
        costs[end-1][start-1] = 0
    
for j in range(n):
    costs[j][j] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(costs[x-1][y-1])