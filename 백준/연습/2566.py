import sys
input = sys.stdin.readline

D = [list(map(int, input().split())) for _ in range(9)]    
maxValue = max(map(max, D))
print(maxValue)

for i in range(0, 9) :
    for j in range(0, 9) :
        if D[i][j] == maxValue:
            print(str(i+1) + " " + str(j+1))

