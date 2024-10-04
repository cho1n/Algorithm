N = int(input())
T = list(map(int, input().split()))

T.sort()

answer = []
start = 0
max_machine = len(T)
if max_machine % 2 != 0:
    end = max_machine - 2
    answer.append(T[max_machine-1])
else:
    end = max_machine - 1

while start < end :
    answer.append(T[start] + T[end])
    start += 1
    end -= 1

print(max(answer))