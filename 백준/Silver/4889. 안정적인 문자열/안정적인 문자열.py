import sys
timer = 1

while True:
    L = list(sys.stdin.readline().rstrip())
    stack = []
    point = 0
    
    if L[0] == '-':
        break
    
    for char in L:
        if char == '{':
            stack.append(char)
        else:
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)

    while stack:
        if stack[-1] == stack[-2]:
            point += 1
        else:
            point += 2
        stack.pop()
        stack.pop()

    
    print(f'{timer}. {point}')
    timer += 1