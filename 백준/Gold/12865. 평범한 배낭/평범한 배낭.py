N, K = map(int, input().split())
items = []

for _ in range(N):
    weight, worth = map(int, input().split())
    items.append((weight, worth))

dp = [0] * (K + 1)

for weight, worth in items:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + worth)

print(dp[K])