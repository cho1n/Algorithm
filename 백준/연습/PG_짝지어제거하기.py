def solution(s):
    answer = 0
    stack = []
    for l in range(len(s)):
        if not stack:
            stack.append(s[l])
            continue

        if stack[-1] == s[l]:
            stack.pop()
        else:
            stack.append(s[l])
    if stack:
        answer = 0
    else:
        answer = 1
    return answer

solution("cdcd")