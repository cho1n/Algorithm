N = int(input())
lopes = []
max_value = 0
for _ in range(N):
    lopes.append(int(input()))

lopes.sort()

    
for l in range(N):
    A = lopes[l] * (N - l)
    if max_value < A:
        max_value = A

print(max_value)