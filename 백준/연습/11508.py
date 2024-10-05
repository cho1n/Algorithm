N = int(input())
cost = []
answer = 0
cnt = 0

for _ in range(N):
    cost.append(int(input()))
    
cost.sort(reverse=True)

for l in cost:
    if cnt != 2:
        answer += l
        cnt += 1
    else:
        cnt = 0

print(answer)