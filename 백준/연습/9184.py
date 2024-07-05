d = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for A in range(21):
    for B in range(21):
        for C in range(21):
            if A <= 0 or B <= 0 or C <= 0:
                d[A][B][C] = 1
            elif A > 20 or B > 20 or C > 20:
                d[A][B][C] = d[20][20][20]
            elif A < B and B < C :
                d[A][B][C] = d[A][B][C-1] + d[A][B-1][C-1] - d[A][B-1][C]
            else:
                d[A][B][C] = d[A-1][B][C] + d[A-1][B-1][C] + d[A-1][B][C-1] - d[A-1][B-1][C-1] 

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1 :
        break
    
    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = d[20][20][20]
    else:
        answer = d[a][b][c]
    
    print(f'w({a}, {b}, {c}) = {answer}')