N = int(input())
A = []
dp = [0] * N
for i in range(N):
    A.append(list(map(int, input().split())))
A.sort()

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i][1] >= A[j][1] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(N - max(dp))
