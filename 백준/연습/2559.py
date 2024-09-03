N, K = map(int, input().split())
temp = list(map(int, input().split()))
start, end = 0, K
sum = 0
ans = 0

while end < N :
    sum = 0
    
    for i in range(start, end):
        sum += temp[i]
    
    if sum > ans:
        ans = sum
        
    start += 1
    end += 1

print(ans)
        