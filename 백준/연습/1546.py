import sys
input = sys.stdin.readline

N = int(input())
M = 0
average = 0
arr = [0] * (N+1)
newArr = [0] * (N+1)

arr = list(map(int, input().split()))

M = max(arr)
for i in range(N):
    newArr[i] = (arr[i] / M)*100
    average = average + (newArr[i]/N)
print(average)
