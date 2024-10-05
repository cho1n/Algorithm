N = int(input())
dp = [0] * 1001
dp[0] = 0
dp[1] = 1
dp[2] = 2

if N >= 3:
    for l in range(3, N+1):
        dp[l] = (dp[l-1] + dp[l-2])%10007

print(dp[N])