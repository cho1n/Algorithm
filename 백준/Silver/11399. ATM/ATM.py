N = input()
arr = list(map(int, input().split()))
temp = 0
ans = 0

arr.sort()

for i in range(int(N)) :
    ans += arr[i]
    temp += ans

print(temp)