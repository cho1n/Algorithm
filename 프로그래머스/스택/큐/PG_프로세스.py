from collections import deque

def solution(priorities, location):
    answer = 0
    list_s = []
    
    pro_queue = deque()
    loc_queue = deque()
    

    for i in priorities:
        pro_queue.append(i)
        
    for i in range(len(priorities)):
        loc_queue.append(i)
           
    while pro_queue:
        pro = pro_queue.popleft()
        loc = loc_queue.popleft()
        
        if len(loc_queue) != 0 and (max(pro_queue) > pro) :
            pro_queue.append(pro)
            loc_queue.append(loc)
        else :
            list_s.append([pro, loc])
            
    for i in range(len(priorities)):
        if list_s[i][1] == location:
            answer = (i+1)
            return answer

print(solution([1, 1, 9, 1, 1, 1],0))