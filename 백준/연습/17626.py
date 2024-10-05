N = int(input())
dp = [50001] * (N+1)
dp[0] = 0

for l in range(1, N+1):
    for j in range(1, l+1):
        val = j * j
        if val > l:
            break
        dp[l] = min(dp[l], dp[l-val] + 1)

print(dp[N])
        