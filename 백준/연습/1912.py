N = int(input())
sequence = list(map(int, input().split()))

for i in range(1, len(sequence)):
    sequence[i] = max(sequence[i-1] + sequence[i], sequence[i])
    
print(max(sequence))