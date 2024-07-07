n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n+1)]
length = 0

for i in range(1, n+1):
    length = len(dp[i-1])
    for j in range(length):
        if j == length:
            answer[i][j] = answer[i-1][j-1] + dp[i-1][j-1]
        elif j == 0:
            answer[i][j] = answer[i-1][j] + dp[i-1][j]
        else:
            answer[i][j] = max(answer[i-1][j-1], answer[i-1][j]) + dp[i-1][j]

print(max(answer[n]))