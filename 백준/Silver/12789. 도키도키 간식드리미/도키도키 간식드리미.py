from collections import deque

N = int(input())
line = list(map(int, input().split()))

mini = 0
pass_line = []
queue = deque(line)
answer = 0

while queue:
    if queue[0] > min(queue):
        v = queue.popleft()
        if v == mini + 1:
            mini = v
            continue
        else:
            pass_line.append(v)
    elif queue[0] == min(queue):
        v = queue.popleft()
        mini = v
        while len(pass_line) != 0 and pass_line[-1] == mini + 1:
            mini = pass_line.pop()
    else:
        answer = 1
        break

if pass_line or answer == 1:
    print("Sad")
else :
    print("Nice")