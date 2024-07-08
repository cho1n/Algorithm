n = int(input())

dp = [0] * n
answer = [0] * (n+1)

for i in range(n):
    m = int(input())
    dp[i] = m


if n >= 3:
    dp.reverse()
    answer[1] = dp[0]
    answer[2] = dp[0] + dp[1]
    answer[3] = dp[2] + dp[0]
        
    for i in range(4, n+1):
        answer[i] = max(answer[i-2], dp[i-2] + answer[i-3]) + dp[i-1]

else : 
    if n == 1:
        answer[1] = dp[0]
    else:
        answer[1] = dp[0]
        answer[2] = dp[0] + dp[1]
        
print(max(answer[n], answer[n-1]))