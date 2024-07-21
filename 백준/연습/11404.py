n = int(input())
m = int(input())
INF = 987654321
costs = [[INF] * (n) for _ in range(n)]

for i in range(m):
    start, end, cost = map(int, input().split())
    costs[start-1][end-1] = min(cost, costs[start-1][end-1])
    

for j in range(n):
    costs[j][j] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

for i in range(n):
    for j in range(n):
        if costs[i][j] == INF :
            print(0, end=' ')
        else :
            print(costs[i][j], end=' ')
    print()