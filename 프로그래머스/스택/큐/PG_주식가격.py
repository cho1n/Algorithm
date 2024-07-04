import copy
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    for i in copy.deepcopy(queue):
        time = 0
        queue.popleft()
        if queue:
            for j in queue:
                if j >= i:
                    time += 1
                else :
                    time += 1
                    break
        answer.append(time)        
    return answer

print(solution([1,2,3,2,3]))