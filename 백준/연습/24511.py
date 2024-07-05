from collections import deque

N = int(input())
queuestack = list(map(int, input().split()))
number_list = list(map(int, input().split()))
answer = []
cnt = 0
num = []
queue = deque()

for i in range(len(number_list)):
    queue.append([i, number_list[i]])

M = int(input())
elements = list(map(int, input().split()))

for j in range(len(queue)):
    if j == 0:
        if queuestack[j] == 0:
                num.append(queue[j][1])
                queue[j][1] = elements[j]
        else:
            num.append(number_list[j])
    else :
        if queuestack[j] == 0:
            
            

