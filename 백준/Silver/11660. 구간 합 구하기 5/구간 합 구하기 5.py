# ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
# D[x][y] = D[x-1][y] + D[x][y-1] - D[x-1][y-1] + A[x][y]

import sys
input = sys.stdin.readline

N, M= map(int, input().split())
A = [[0] * (N+1)] # 1차원 배열선언
D = [[0] * (N+1) for _ in range(N+1)] # 2차원 배열선언

for i in range(N) :
    A_row = [0] + [int(x) for x in input().split()] # row 한줄에 다 받기
    A.append(A_row) # 1차원 배열에 추가
    
for i in range(1, N+1) :
    for j in range(1, N+1) :
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)