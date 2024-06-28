money = []
count = 0
cnt = 0

N, K = map(int, input().split())

for i in range(N):
    cash = int(input())
    money.append(cash)

moneys = sorted(money, reverse=True)

while True:
    if cnt < len(money) and moneys[cnt] <= K :
        K -= moneys[cnt]
        count += 1
        cnt = 0
    else:
        cnt += 1
    
    if K == 0:
        break
    
print(count)