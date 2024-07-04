# from collections import deque

# def solution(bridge_lengeth, weight, truck_weights):
#     answer = 0
        
#     truck_queue = deque()
#     crossing_queue = deque()
#     truck_list = truck_weights[:]
    
#     for i in truck_list:
#         truck_queue.append(i)
    
#     for i in range(len(truck_list)):
#         if truck_queue:
#             limit_weight = 0
#             truck = truck_queue.popleft()
            
#             limit_weight += truck            
#             crossing_queue.append(truck)
            
#             if i != len(truck_list):
#                 for j in range(i+1, len(truck_list)):
#                     limit_weight += truck_list[j]
#                     if truck_queue and limit_weight <= weight:
#                         crossing_queue.append(truck_queue.popleft())
#                         answer += 1
            
#             answer += bridge_lengeth
#             while crossing_queue:
#                 crossing_queue.popleft()
            
#         else :
#             break
    
#     return answer

# print(solution(3, 3, [1, 2, 3]))

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    complete = []

    qu_truck = deque(truck_weights)
    loading = deque()
    loading_time = deque()

    while True:
        time += 1

        if loading and time-loading_time[0] == bridge_length:
            complete.append(loading.popleft())
            loading_time.popleft()

            if complete == truck_weights:
                return time

        if len(qu_truck) >= 1 and sum(loading) + qu_truck[0] <= weight :
            loading.append(qu_truck.popleft())
            loading_time.append(time)