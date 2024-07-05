n = int(input())

dp = [0] * (n+1)

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    if i >= 15746:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    else:
        dp[i] = dp[i-1] + dp[i-2]

answer = dp[n-1]

print(answer)