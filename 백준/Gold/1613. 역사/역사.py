n, k = map(int, input().split())
INF = 987654321
costs = [[INF] * n for _ in range(n)]

for i in range(k):
    ahead, last = map(int, input().split())
    costs[ahead-1][last-1] = 1
    
for j in range(n):
    costs[j][j] = 0
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

s = int(input())

for i in range(s):
    start, end = map(int, input().split())
    if costs[start-1][end-1] + costs[end-1][start-1] == 2 * INF:
        print(0)
    elif costs[start-1][end-1] > 0 and costs[start-1][end-1] < INF and costs[end-1][start-1] == INF :
        print(-1)
    else:
        print(1)