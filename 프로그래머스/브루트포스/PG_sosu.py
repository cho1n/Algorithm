from itertools import permutations
import math

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True        

def solution(numbers):
    answer = 0
    used = [False] * 10000000
    decimal = []
    numbers_list = []
    conList = []
    
    for i in numbers:
        numbers_list.append(i)
    
    for i in range(1, len(numbers_list)+1):
        conList += list(permutations(numbers_list, i))
    
    midList = []
    for i in conList :
        midList.append(int(''.join(i)))
    
    for i in range(len(midList)):
        if is_prime(midList[i]) and used[int(midList[i])] == False :
            if midList[i] != 1 and midList[i] != 0:
                decimal.append(midList[i])
                used[int(midList[i])] = True
        
    answer = len(decimal)
    return answer