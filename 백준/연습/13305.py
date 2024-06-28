N = int(input())
road = list(map(int, input().split()))
town = list(map(int, input().split()))
start = town[0] * road[0]
cost = 0
k = 0

for i in range(len(road)):
    if town[k] < town[i]:
        cost = cost + (town[k] * road[i])
    else :
        k = i
        cost = cost + (town[i] * road[i])
        
print(cost)