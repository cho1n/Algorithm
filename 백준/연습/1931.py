N = int(input())
time_table = []

for i in range(N):
    s, e = map(int, input().split())
    time_table.append([e, s])

time_table.sort()
t = time_table[0][0]
cnt = 1

for i in range(1, N):
    if t <= time_table[i][1]:
        t = time_table[i][0]
        cnt += 1

print(cnt)