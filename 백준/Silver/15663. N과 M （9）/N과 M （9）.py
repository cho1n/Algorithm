N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
ans = []
arr.sort()

def back():
    check = 0
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if check != arr[i] and visited[i] == 0:
            ans.append(arr[i])
            visited[i] = True
            check = arr[i]
            back()
            ans.pop()
            visited[i] = 0
        
back()