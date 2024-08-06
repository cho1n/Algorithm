n = int(input())
arr = list(map(int, input().split()))
target = int(input())
arr.sort()
start, end = 0, n-1
ans = 0

while start < end:
    sum = arr[start] + arr[end]
    if sum > target:
        end -= 1
    elif sum < target:
        start += 1
    elif sum == target:
        ans += 1
        start += 1
        end -= 1

print(ans)