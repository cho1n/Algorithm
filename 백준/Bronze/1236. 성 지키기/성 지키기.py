import sys

N, M = map(int, input().split())
kingdom = []

for _ in range(N):
    kingdom.append(list(sys.stdin.readline().strip()))

row_count = 0
for i in range(N):
    if "X" not in kingdom[i]:
        row_count += 1

col_count = 0
for j in range(M):
    if "X" not in [kingdom[i][j] for i in range(N)]:
        col_count += 1

print(max(row_count, col_count))