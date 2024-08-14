def bingo_check(bingo_list): # 부른 숫자 체크 0으로
    global count, bingo, ans
    
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if bingo_board[j][k] == bingo_list[i]:
                    bingo_board[j][k] = 0
                    bingo = 0
                    count += 1
                    find_x_bingo()
                    find_y_bingo()
                    find_x_y_bingo()
                    find_y_x_bingo()
                    if bingo >= 3:
                        ans.append(count)
                        
                else:
                    continue
    
def find_x_bingo(): # 옆    
    global bingo
    
    if bingo < 3:
        for i in range(5):
            x_count = 0
            if bingo_board[i][0] == 0:
                x_count += 1
                for j in range(1, 5):
                    if bingo_board[i][j] == 0:
                        x_count += 1
                    else:
                        continue
            if x_count == 5:
                bingo += 1


def find_y_bingo(): # 아래
    global bingo
    if bingo < 3 :
        for i in range(5):
            y_count = 0
            if bingo_board[0][i] == 0:
                y_count += 1
            for j in range(1,5):
                if bingo_board[j][i] == 0:
                    y_count += 1
                else:
                    continue
            if y_count == 5:
                bingo += 1

def find_y_x_bingo(): # 우측 대각
    global bingo
    if bingo < 3 :
        y_x_count = 0
        if bingo_board[0][0] == 0:
            y_x_count += 1
            for i in range(1, 5):
                if bingo_board[i][i] == 0:
                    y_x_count += 1
        if y_x_count == 5:
            bingo += 1
    
def find_x_y_bingo(): # 좌측 대각
    global bingo
    x_y_count = 0
    x = 4
    y = 0
    if bingo < 3 :
        if bingo_board[y][x] == 0:
            x_y_count += 1
            x -= 1
            y += 1
            for _ in range(4):
                if bingo_board[y][x] == 0:
                    x -= 1
                    y += 1
                    x_y_count += 1
        if x_y_count == 5:
            bingo += 1

bingo_board = [] # 빙고판
count = 0
bingo = 0
ans = []

for _ in range(5):
    row = list(map(int, input().split())) 
    bingo_board.append(row)

for _ in range(5):
    check = list(map(int, input().split()))
    bingo_check(check)

print(ans[0])