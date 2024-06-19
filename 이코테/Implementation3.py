N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[x][y] = 1
steps = [0, 1, 2, 3] #북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for step in steps:
    print(step)