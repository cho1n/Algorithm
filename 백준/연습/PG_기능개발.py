from collections import deque

def solution(progresses, speeds):
    answer = []
    progress_queue = deque()
    for i in range(len(progresses)):
        progress_queue.append(progresses[i])
    
    speeds_queue = deque()
    for i in range(len(speeds)):
        speeds_queue.append(speeds[i])

    while progress_queue: 
        count = 0
        
        for i in range(len(progress_queue)):
            progress_queue[i] += speeds_queue[i]
        
        if progress_queue[0] >= 100:
            while len(progress_queue) != 0 and (progress_queue[0] >= 100):
                progress_queue.popleft()
                speeds_queue.popleft()
                count += 1
            if count >= 0 :
                answer.append(count)      
          
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))