N = int(input())
dp = [0] * 91
dp[0] = 0
dp[1] = 1
dp[2] = 1

for l in range(3, N+1):
    dp[l] = dp[l-1] + dp[l-2]

print(dp[N])