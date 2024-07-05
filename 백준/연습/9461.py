T = int(input())

dp = [0] * 101

dp[0], dp[1], dp[2] = 1, 1, 1
dp[3], dp[4] = 2, 2

for i in range(5, len(dp)):
    dp[i] = dp[i-3] + dp[i-4] + dp[i-5]

for i in range(T):
    N = int(input())
    print(dp[N-1])
    
