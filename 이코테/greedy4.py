N, K = map(int, input().split())
cnt = 0
flag = 0
while N != 1 :
    while N%K==0 and N >= K :
        N = N // K
        cnt += 1
    if(N==1):
        flag = 1
    if(flag):
        break
    N -= 1
    cnt += 1
print(cnt)