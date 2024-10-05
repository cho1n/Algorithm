T = int(input())
dp = [[0] * 30 for _ in range(30)]

for _ in range(T):
    N, M = map(int, input().split())
    
    for l in range(0, M+1):
        for k in range(0, l+1):
            if k == 0 or k == l:
                dp[l][k] = 1
            else:
                dp[l][k] = dp[l-1][k-1] + dp[l-1][k]
                
    print(dp[M][N])