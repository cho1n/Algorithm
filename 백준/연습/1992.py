import sys

N = int(input())
quadTree = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
result = []

def solution(x, y, N):
    color = quadTree[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != quadTree[i][j]:
                result.append("(")
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                result.append(")")
                return
    if color == 1:
        result.append(1)
    else:
        result.append(0)


solution(0, 0, N)
for i in range(len(result)):
    print(result[i], end="")