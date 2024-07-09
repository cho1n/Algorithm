n=int(input())
w=[0]*10000
for i in range(n):
    w[i]=int(input())
dp = [0]*10000

dp[0] = w[0]
dp[1] = w[0] + w[1]
dp[2] = max(dp[1], w[0] + w[2], w[1] + w[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], w[i] + dp[i-2], w[i] + w[i-1] + dp[i-3])
print(dp[n-1])