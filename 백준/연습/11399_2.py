N = int(input())
members = list(map(int, input().split()))
time = 0
times = []
result = 0

member = sorted(members)

for i in range(N):
    time += member[i]
    times.append(time)

for i in range(len(times)):
    result += times[i]

print(result)