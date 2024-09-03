N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

start, end = 0, N - 1
min_sum = 2000000001
ans = (0, 0)

while start < end:
    sum = liquid[start] + liquid[end]

    if abs(sum) < abs(min_sum):
        min_sum = sum
        ans = (liquid[start], liquid[end])
    
    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1
    else:
        break

if N == 2:
    print(liquid[0], liquid[1])
else:
    print(ans[0], ans[1])
