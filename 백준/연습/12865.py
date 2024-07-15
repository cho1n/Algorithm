# N, K = map(int, input().split())
# weights = []
# worth = []
# max_worth = 0

# for i in range(N):
#     a, b = map(int, input().split())
#     weights.append(a)
#     worth.append(b)
    

# dp1 = [[0] * (len(weights) + 1) for _ in range(len(weights) + 1)]
# dp2 = [[0] * (len(worth) + 1) for _ in range(len(worth) + 1)]


# for i in range(1, len(weights)+1):
#     for j in range(1, len(weights)+1):
#         if i == j:
#             dp1[i][j] = weights[i-1]
#             dp2[i][j] = worth[i-1]
#         else:
#             if dp1[i][j-1] + weights[j-1] <= K:
#                 dp1[i][j] = weights[j-1] + dp1[i][j-1]
#                 dp2[i][j] = worth[j-1] + dp2[i][j-1]
#                 if dp2[i][j] > max_worth:
#                     max_worth = dp2[i][j]
#             else:
#                 if max(worth[i-1], worth[j-1]) == worth[i-1]:
#                     dp2[i][j] = worth[i-1]
#                     dp1[i][j] = weights[i-1]
#                 else:
#                     dp2[i][j] = worth[j-1]
#                     dp1[i][j] = weights[j-1]

# if N == 1 :
#     print(worth[0])    
# else:
#     print(max_worth)

N, K = map(int, input().split())
items = []

for _ in range(N):
    weight, worth = map(int, input().split())
    items.append((weight, worth))

dp = [0] * (K + 1)

for weight, worth in items:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + worth)
        print(dp)

print(dp[K])
