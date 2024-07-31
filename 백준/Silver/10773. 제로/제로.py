K = int(input())
stack = []

for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    elif len(stack) != 0 and num == 0 :
        stack.pop()

print(sum(stack))