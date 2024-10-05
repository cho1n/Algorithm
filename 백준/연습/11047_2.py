N,K = map(int, input().split())
money = []
max_range = N - 1
answer = 0
for _ in range(N):
    money.append(int(input()))

money.sort()

while True:
    
    if K - money[max_range] >= 0:
        K -= money[max_range]
        answer += 1
    else:
        max_range -= 1
    
    if K == 0:
        break
    
print(answer)