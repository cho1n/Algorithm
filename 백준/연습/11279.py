import heapq
heap = []

T = int(input())

for _ in range(T):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))

    
        
    
