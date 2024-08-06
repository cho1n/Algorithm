import sys
L = list(sys.stdin.readline().rstrip())
left_stack = []
right_stack = []
answer = []
ans = 0
flag = 0
temp = 0

for char in L:

    if char == '[' or char == '(':
        if not left_stack:
            temp = 0
            left_stack.append(char)
        else:
            if right_stack:
                outer = right_stack.pop()
                left_stack.append(outer)
                right_stack.append(char)
            else:
                right_stack.append(char)

    else:
        if char == ')':
            if len(right_stack) != 0 and right_stack[-1]  != '(':
                print(0)
                flag = 1
                break
            elif len(right_stack) != 0 and right_stack[-1] == '(':
                right_stack.pop()
                ans += 2
                if left_stack:
                    temp = 1
                    for chars in left_stack:
                        if chars == '(':
                            ans *= 2
                        else:
                            ans *= 3
                answer.append(ans)
                ans = 0
                temp = 1
                
            elif len(left_stack) != 0 and left_stack[-1] == '(':
                left_stack.pop()
                if temp == 0:
                    ans += 2
                    answer.append(ans)
                    ans = 0
            else:
                print(0)
                flag = 1
                break
                
        elif char == ']':
            if len(right_stack) != 0 and right_stack[-1]  != '[':
                print(0)
                flag = 1
                break
            elif len(right_stack) != 0 and right_stack[-1] == '[':
                right_stack.pop()
                ans += 3
                if left_stack:
                    temp = 1
                    for chars in left_stack:
                        if chars == '(':
                            ans *= 2
                        else:
                            ans *= 3
                answer.append(ans)
                ans = 0
                temp = 1
                
            elif len(left_stack) != 0 and left_stack[-1] == '[':
                left_stack.pop()
                if temp == 0:
                    ans += 3
                    answer.append(ans)
                    ans = 0
            else:
                print(0)
                flag = 1
                break
            
    if not left_stack:
        answer.append(ans)
        ans = 0
    
if len(left_stack) == 0 and len(right_stack) == 0 and flag == 0:
    print(sum(answer))
elif (len(left_stack) != 0 or len(right_stack) != 0) and flag == 0 :
    print(0)