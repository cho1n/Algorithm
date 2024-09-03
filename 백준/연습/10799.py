import sys
lines = list(sys.stdin.readline().rstrip())

stack = []
ans = 0

for i in range(len(lines)):
    if lines[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if lines[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)
