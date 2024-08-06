import sys
input = sys.stdin.readline

def calculate_bracket_value(brackets):
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(brackets)):
        char = brackets[i]
        
        if char == '(':
            stack.append(char)
            temp *= 2
        
        elif char == '[':
            stack.append(char)
            temp *= 3
        
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0
            if brackets[i - 1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if brackets[i - 1] == '[':
                result += temp
            stack.pop()
            temp //= 3
    
    if stack:
        return 0
    
    return result

brackets = input().strip()
print(calculate_bracket_value(brackets))
