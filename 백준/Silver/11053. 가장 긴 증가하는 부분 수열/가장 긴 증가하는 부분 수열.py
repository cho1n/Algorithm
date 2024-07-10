N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
max = 1

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            if max < dp[i]:
                max = dp[i]

print(max)