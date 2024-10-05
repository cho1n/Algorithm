N = int(input())
dp = [0] * 1000001
dp[0] = 0


for l in range(2, N+1):
    dp[l] = dp[l-1] + 1

    if l%3 == 0:
        dp[l] = min(dp[l], dp[l//3] + 1)
    if l%2 == 0:
        dp[l] = min(dp[l], dp[l//2] + 1)

print(dp[N])