# n = int(input())
# arr = [0] * n

# dp = [[0] * (n+1) for _ in range(n+1)]
# answer = [0] * (n+1)

# for i in range(n):
#     arr[i] = int(input())

# for i in range(n):
#     length = len(arr[i:])
#     for j in range(length):
#         dp[i][j] = arr[i + j]
#     for j in range(length, n):
#         dp[i][j] = 0

# if n == 1:
#     print(arr[0])
# elif n == 2:
#     print(arr[0] + arr[1])
# elif n == 3:
#     print(max(arr[0]+arr[1], arr[0]+arr[2]))
# else:
#     for i in range(n):
#         for j in range(n):
#             if j == 0:
#                 dp[i][0] = dp[i][0]
#             elif j == 1:
#                 dp[i][1] = max(dp[i][0] + dp[i][1], dp[i][1])
#             elif j == 2:
#                 dp[i][2] = max(dp[i][0] + dp[i][1], dp[i][0] + dp[i][2], dp[i][2])
#             else:
#                 dp[i][j] = max(dp[i-3] )   
    
# print(dp)

n=int(input())
w=[0]*10000
for i in range(n):
    w[i]=int(input())
dp = [0]*10000

dp[0] = w[0]
dp[1] = w[0] + w[1]
dp[2] = max(dp[1], w[0] + w[2], w[1] + w[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], w[i] + dp[i-2], w[i] + w[i-1] + dp[i-3])
print(dp[n-1])