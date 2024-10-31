N = int(input())
people = []
ans = []

for _ in range(N):
    x, y = map(int, input().split())
    people.append([x, y])
    
for l in range(N):
    cnt = 1
    for k in range(N):
        if l == k:
            continue
        if people[l][0] < people[k][0] and people[l][1] < people[k][1] :
            cnt += 1
    ans.append(cnt)

for l in range(len(ans)):
    print(ans[l], end=' ')