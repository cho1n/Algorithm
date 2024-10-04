s = input()
s_arr = []
cnt = 0
answer = ""
flag = 1

for i in s:
    s_arr.append(i)

while True:
    if s[cnt:cnt+4] == "XXXX":
        for i in range(cnt, cnt+4):
            s_arr[i] = 'A'
            if i == cnt + 3:
                cnt = i + 1
    elif s[cnt:cnt+2] == "XX":
        for j in range(cnt, cnt+2):
            s_arr[j] = 'B'
            if j == cnt + 1:
                cnt = j + 1
    else:
        cnt += 1
    
    if cnt == len(s):
        break
    
for l in s_arr:
    answer += l
    if l == 'X':
       flag = 0

if flag:
    print(answer)
else:
    print(-1)