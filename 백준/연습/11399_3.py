N = int(input())
times = list(map(int, input().split()))
answer = 0

times.sort()

for t in range(len(times)):
    for i in range(0, t+1):
        answer += times[i]

print(answer)