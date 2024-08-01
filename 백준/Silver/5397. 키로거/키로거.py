import sys

T = int(input())
for _ in range(T):
    L = list(sys.stdin.readline().rstrip())
    left_stack = []
    right_stack = []
    
    for char in L:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
    
    ans = ''.join(left_stack) + ''.join(reversed(right_stack))
    print(ans)