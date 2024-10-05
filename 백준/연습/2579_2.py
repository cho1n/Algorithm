N = int(input())
dp = [0]
cnt = 1
for l in range(N):
    dp.append(int(input()))
    
dp.reverse()
dp.insert(0, 0)


if N > 1:
    dp[2] += dp[1]
    dp[3] += dp[1]

    for i in range(4, N+1):
        if ( dp[i-1] + dp[i] > dp[i-2] + dp[i] ) and cnt < 2 :
            cnt += 1
            dp[i] = dp[i-1] + dp[i]
        else:
            cnt = 1
            dp[i] = dp[i-2] + dp[i]

    print(max(dp[N], dp[N-1]))
else:
    print(dp[1])