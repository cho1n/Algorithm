N = int(input())
dp = [0] * (N+1)
for l in range(1, len(dp)):
    if l > 5:
        dp[l] = min(dp[l-5]+1, dp[l-3]+1)
    else:
        if l == 3 or l == 5:
            dp[l] = 1
        else:
            dp[l] = 9999

if dp[N] < 9999 and not 0:
    print(dp[N])
else:
    print(-1)