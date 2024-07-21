t = int(input())
INF = 0

for i in range(t):
    costs = [[INF] * 65535 for _ in range(65535)]
    n = int(input())
    x, y = map(int, input().split())
    costs[x][y] = 0
    s_x, s_y = map(int, input().split())
    costs[s_x][s_y] = 0
    f_x, f_y = map(int, input().split())
    costs[f_x][f_y] = 0
    
    for j in range(costs[0]):
        for k in range(costs[0]):
            for l in range(costs[0]):
                costs[k][l] = min(costs[k][l], costs[k][j] + costs[j][l])
    
    print(costs[f_x][f_y])