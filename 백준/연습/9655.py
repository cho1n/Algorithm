N = int(input())
dp = [0] * (N+1)

if N == 1:
    dp[1] = 1
    
elif N == 2:
    dp[1] = 1
    dp[2] = 0
    
elif N == 3:
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1
    
else:
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1

    for l in range(4, len(dp)):
        if dp[l-3] == 0 or dp[l-1] == 0:
            dp[l] = 1
        else:
            dp[l] = 0

if dp[N]:
    print("SK")
else:
    print("CY")