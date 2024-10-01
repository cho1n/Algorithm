right = [['y','u','i','o','p'], # 모음 y u i o p 
            ['h','j','k','l'], # 모음 h j k l
            ['b','n','m']] # 모음 b n m
left = [['q', 'w', 'e', 'r', 't'],
         ['a','s','d','f','g'],
         ['z','x','c','v']
        ]

left_location={left[i][j]:(i,j) for i in range(3) for j in range(len(left[i]))}
right_location = {right[i][j]: (i, j + 1 if i != 2 else j) for i in range(3) for j in range(len(right[i]))}        
        
sL, sR = map(str, input().split())
s = input()
s_left = [sL]
s_right = [sR]
sL_location = (0, 0)
sR_location = (0, 0)
time = 0

for i in s:
    for j in range(3):
        if i in left[j]:
            s_left.append(i)
        elif i in right[j]:
            s_right.append(i)

for i in range(len(s_left)-1):
    x1, y1 = left_location[s_left[i]]
    x2, y2 = left_location[s_left[i+1]]
    time += (abs(x1-x2) + abs(y1-y2)) + 1
for i in range(len(s_right)-1):
    x1, y1 = right_location[s_right[i]]
    x2, y2 = right_location[s_right[i+1]]
    time += (abs(x1-x2) + abs(y1-y2)) + 1
print(time)