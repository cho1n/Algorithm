V, E = map(int, input().split())
INF = 987654321
ans = 987654321
costs = [[INF] * V for _ in range(V)]

for i in range(E):
    start, end, cost = map(int, input().split())
    costs[start-1][end-1] = cost

for j in range(V):
    costs[j][j] = 0

for i in range(V):
    for j in range(V):
        for k in range(V):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

for i in range(V):
    for j in range(V):
        if costs[i][j] + costs[j][i] >= INF :
            continue
        else:
            if ans > (costs[i][j] + costs[j][i]) and costs[i][j] + costs[j][i] != 0:
                ans = costs[i][j] + costs[j][i]

if ans == INF :
    print(-1)
else:
    print(ans)