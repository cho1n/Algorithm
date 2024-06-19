N, M = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]    
minValue = []

for i in range(N):
    minValue.append(min(D[i]))

print(max(minValue))
    