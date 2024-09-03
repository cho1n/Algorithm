import sys
left_stack = list(sys.stdin.readline().rstrip())
M = int(input())
right_stack = []

for _ in range(M):
    commend = input().split()
    if commend[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif commend[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif commend[0] == 'B':
        if left_stack:
            left_stack.pop()
    else:
        left_stack.append(commend[1])


ans = ''.join(left_stack) + ''.join(reversed(right_stack))
print(ans)