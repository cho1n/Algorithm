N = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)
answer = drink[0]


for l in range(1, len(drink)):
    answer += drink[l]/2

if int(answer) == answer:
    print(int(answer))
else:
    print(answer)