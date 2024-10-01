import heapq

def calc(x):
    s, e = x[0], x[1]
    total_s = int(s[:2]) * 60 + int(s[3:])
    total_e = int(e[:2]) * 60 + int(e[3:])
    
    return [total_s, total_e]

def solution(book_time):
    time_table = []
    q = []
    
    for i in range(len(book_time)):
        K = calc(book_time[i])
        time_table.append(K)
    
    time_table.sort()
    heapq.heappush(q, time_table[0][1])
            
    for i in range(1, len(time_table)):
        if q[0] + 10 <= time_table[i][0]:
            heapq.heappop(q)
        heapq.heappush(q, time_table[i][1])
    
    return len(q)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))