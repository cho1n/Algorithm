def solution(arr):
    answer = []
    stack = []
    stack.append(arr[0])
    
    for i in range(1, len(arr)):
        if stack[-1] == arr[i]:
            continue
        else:
            stack.append(arr[i])
    
    answer = stack     
    return answer

print(solution([4,4,4,3,3]	))