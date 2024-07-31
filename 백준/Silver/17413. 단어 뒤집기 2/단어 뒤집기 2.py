import sys
S = list(sys.stdin.readline().rstrip())
flag = 0
stack = []
ans = ""

for i in range(len(S)):
    if S[i] == '<':
        flag = 1
        ans += S[i]
    elif S[i] == '>':
        flag = 0
        ans += S[i]
    elif flag == 0 and S[i] == ' ':
        while stack:
            ans += stack.pop()
        stack.append(S[i])
        ans += stack.pop()
    elif flag == 0 and S[i] != ' ':    
        stack.append(S[i])
        if i < len(S) - 1 and S[i+1] == '<':
            while stack:
                ans += stack.pop()
    elif flag == 1 :
        ans += S[i]

if stack:
    while stack:
        ans += stack.pop()
    
print(ans)