N = int(input())
A = list(map(int, input().split()))
A_reverse = list(reversed(A))
dp = [0] * N
dp_s = [0] * N
answer = [0] * N
max_s = 1
min = 1
index = 0

for i in range(N):
    dp[i] = 1
    dp_s[i] = 1
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            if max_s < dp[i]:
                max_s = dp[i]
                index = i
        if A_reverse[j] < A_reverse[i] and dp_s[j] + 1 > dp_s[i]:
            dp_s[i] = dp_s[j] + 1
            if min < dp_s[i]:
                min = dp_s[i]

for i in range(N):
    answer[i] = dp[i] + dp_s[N - i - 1] - 1

if max_s == 0:
    print(min)
elif min == 0:
    print(max_s)
else :
    print(max(answer))