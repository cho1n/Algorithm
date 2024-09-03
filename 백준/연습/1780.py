N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split(' '))))
    
result = []

def solution(x,y,N):
    num = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != paper[i][j]:
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+(2*N//3), N//3)
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+(2*N//3), N//3)
                solution(x+(2*N//3), y, N//3)
                solution(x+(2*N//3), y+N//3, N//3)
                solution(x+(2*N//3), y+(2*N//3), N//3)
                return
    if num == 1:
        result.append(1)
    elif num == 0:
        result.append(0)
    else:
        result.append(-1)

solution(0,0,N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))