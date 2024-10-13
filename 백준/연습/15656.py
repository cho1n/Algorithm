N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(0, len(arr)):
        ans.append(arr[i])
        back()
        ans.pop()
        
back()