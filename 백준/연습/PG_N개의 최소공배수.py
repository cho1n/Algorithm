import math

def solution(arr):
    arr.sort(reverse = True)
    answer = [0]
    answer.append((arr[0] * arr[1]) // math.gcd(arr[0], arr[1]) )
    
    for l in range(1, len(arr)-1):
        N = (arr[l] * answer[l]) // math.gcd(arr[l], answer[l]) 
        answer.append(N)
    
    return max(answer)

solution([2,6,8,14])
    
