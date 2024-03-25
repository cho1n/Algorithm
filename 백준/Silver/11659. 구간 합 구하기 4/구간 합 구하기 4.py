import sys
input = sys.stdin.readline

N, M= map(int, input().split())
A = [0] * (N+1)
D = [0] * (N+1)

A = list(map(int, input().split()))
D[0] = A[0]

for i in range(1, N) :
    D[i] = A[i] + D[i-1]

for _ in range(M) :
    i, j = map(int, input().split())
    result = D[j-1] - D[i-2]
    print(result)