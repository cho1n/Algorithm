N, M = map(int, input().split())
dp = [[0] * 101 for _ in range(101)]

for i in range(1, 101):
    for j in range(1, i+1):
        if i == j:
            dp[i][j] = 1
        elif j == 1:
            dp[i][1] = i
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[N][M])
