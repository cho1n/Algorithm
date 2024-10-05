N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()

def back(start):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, len(arr)):
        ans.append(arr[i])
        back(i)
        ans.pop()
        
back(0)