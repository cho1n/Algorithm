N, M, K = map(int, input().split())
arr = []
arr = list(map(int, input().split()))
cnt = 0
result = 0
arr.sort()
flag = 0
if M>=K :
    while cnt < M:
        for i in range(K):
            result += arr[-1]
            cnt += 1
            if(cnt == M):
                break
        if(cnt == M):
            break
        result += arr[-2]
        cnt += 1
    print(result)
    
        