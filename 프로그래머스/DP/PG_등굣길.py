def solution(m, n, puddles):
    limit = 1000000007
    dp = [[0] * (101) for _ in range(101)]
    for i, j in puddles:
        dp[i][j] = -1
    
    for i in range(1, m+1):
        if dp[i][1] != -1:
            dp[i][1] = 1
        else:
            break
    for j in range(1, n+1):
        if dp[1][j] != -1:
            dp[1][j] = 1
        else:
            break    
    
    for i in range(2, m+1):
        for j in range(2, n+1):
            if dp[i][j] == -1 :
                continue
            elif dp[i-1][j] == -1 and dp[i][j-1] == -1:
                dp[i][j] = 0
            elif dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return (dp[m][n] % limit) 

print(solution(4, 3, [[2,2]]))