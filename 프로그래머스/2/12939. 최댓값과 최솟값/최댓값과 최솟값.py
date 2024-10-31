import sys
from collections import deque

def solution(s):
    A = list(s.split())
    B = deque()
    max = -99999999
    min = 99999999
    answer = ""
    
    for i in range(len(A)):
        
        if int(A[i]) > max:
            max = int(A[i])
        
        if int(A[i]) < min:
            min = int(A[i])
    
    B.append(str(min))
    B.append(str(max))
    
    answer = B.popleft() + " " + B.popleft()
            
    return answer