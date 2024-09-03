# import sys
# T = int(input())

# for i in range(T):
#     L = list(sys.stdin.readline().rstrip())
#     idx = 0
#     stack = []
#     ans = ""
#     for j in range(len(L)):
#         if L[j] == '<':
#             if idx > 0:
#                 idx -= 1
#             else :
#                 continue
#         elif L[j] == '>':
#             idx += 1
#             if idx > len(stack):
#                 idx = len(stack)
#         elif L[j] == '-':
#             if stack:
#                 stack.pop(idx-1)
#                 idx -= 1
#         else:
#             stack.insert(idx, L[j])
#             idx += 1
#             if idx > len(stack):
#                 idx = len(stack)
    
#     ans = ''.join(stack)
#     print(ans)
    
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