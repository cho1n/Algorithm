N, M = map(int, input().split())
INF = 987654321
costs = [[INF] * (N) for _ in range(N)]
count = 0

for i in range(M):
    short, long = map(int, input().split())
    costs[short-1][long-1] = 1

for j in range(N):
    costs[j][j] = 0
    
for i in range(N):
    for j in range(N):
        for k in range(N):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

for i in range(N):
    for j in range(N):
        if costs[i][j] == INF and costs[j][i] != INF:
            costs[i][j] = costs[j][i]

for i in range(N):
    if sum(costs[i]) < INF:
        count += 1

print(count)