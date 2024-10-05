N = int(input())
dist = list(map(int, input().split()))
towns = list(map(int, input().split()))
answer = 0
min_oil = towns[0]

for d in range(len(dist)):
    if min_oil > towns[d]:
        min_oil = towns[d]
    answer += min_oil * dist[d]
            
print(answer)