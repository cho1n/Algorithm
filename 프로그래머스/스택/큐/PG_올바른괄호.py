def solution(s):
    answer
    stack = []
    
    for i in s:
        if i == "(":
           stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                answer = False
                return answer
            else :
                stack.pop()

    if len(stack) != 0:
        answer = False
        return answer
    else:
        answer = True
        return answer