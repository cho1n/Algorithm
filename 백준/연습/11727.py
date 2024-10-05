N = int(input())

dp = [0] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 3
dp[3] = 5

for l in range(4,N+1):
    dp[l] = ((dp[l-2]*2) + dp[l-1]) % 10007

print(dp[N])