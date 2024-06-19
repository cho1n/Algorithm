N = int(input())
leave = N%5
ans = 0

if N > 10 :
    while N != leave:
        N = N - 5
        ans += 1
        
    while N > 0:
        if N % 3 != 0 :
            N = N + 5
            ans -= 1
        elif N % 3 == 0 :
            N = N - 3
            ans += 1
        else :
            print(-1)
    print(ans)
    
else :
    while N>2 :
        if N%5 == 0:
            N = N - 5
            ans += 1
        elif N%3 == 0 :
            N = N - 3
            ans += 1
        else :
            if (N-5)%3 == 0:
                N = N - 3
                ans +=1
            elif (N-3) % 5 == 0:
                N = N -5
                ans +=1
            else:
                print(-1)
                break    
    if ans > 0 :
        print(ans)

