n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
answer = [[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    answer[i][0] = min(answer[i-1][1],answer[i-1][2])+dp[i-1][0]
    answer[i][1] = min(answer[i-1][0],answer[i-1][2])+dp[i-1][1]
    answer[i][2] = min(answer[i-1][0],answer[i-1][1])+dp[i-1][2]

print(min(answer[n][0],answer[n][1],answer[n][2]))
