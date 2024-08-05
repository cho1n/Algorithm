import sys

while True:

    L = list(sys.stdin.readline().rstrip())
    stack = []
    
    if L[0] == '.':
        break

    for char in L:
        if char == '(' or char == '[' or char == '.':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0 or stack[-1] != '[':
                break
            else:
                stack.pop()
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                break
            else:
                stack.pop()

    if len(stack) == 1 and stack[0] == '.':
        print("yes")
    else:
        print("no")