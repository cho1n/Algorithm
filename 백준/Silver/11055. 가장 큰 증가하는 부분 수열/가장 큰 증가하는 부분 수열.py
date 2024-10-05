N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
max_value = 0

for i in range(N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
            if dp[i] > max_value:
                 max_value = dp[i]

print(max(dp))