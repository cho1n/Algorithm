quack = [['q', 0], ['u', 0], ['a', 0], ['c', 0], ['k', 0]]
s = input()
    
flag = 1
duck_count = 0

for l in s:
    if l == 'q':
        quack[0][1] += 1
    elif l == 'u':
        if quack[0][1] > quack[1][1]:
            quack[1][1] += 1
        else:
            flag = 0
            break
    elif l == 'a':
        if quack[1][1] > quack[2][1]:
            quack[2][1] += 1
        else:
            flag = 0
            break
    elif l == 'c':
        if quack[2][1] > quack[3][1]:
            quack[3][1] += 1
        else:
            flag = 0
            break
    elif l == 'k':
        if quack[3][1] > quack[4][1]:
            quack[4][1] += 1
            duck_count = max(duck_count, quack[0][1])
            quack[0][1] -= 1
            quack[1][1] -= 1
            quack[2][1] -= 1
            quack[3][1] -= 1
            quack[4][1] -= 1
        else:
            flag = 0
            break
        
if not (quack[0][1] == quack[1][1] == quack[2][1] == quack[3][1] == quack[4][1]):
    flag = 0
    
if flag:
    print(duck_count)
else:
    print(-1)