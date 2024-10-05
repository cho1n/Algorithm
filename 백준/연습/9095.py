T = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    N = int(input())
    
    for l in range(1, len(dp)):
        if l == 1:
            dp[l] = 1
        elif l == 2:
            dp[l] = 2
        elif l == 3 :
            dp[l] = 4
        else:
            dp[l] = dp[l-3] + dp[l-2] + dp[l-1]
    
    print(dp[N])
        