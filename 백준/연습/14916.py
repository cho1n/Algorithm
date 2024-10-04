n = int(input())
count = 0
flag = 1

while True:
    if n == 3 or n < 2 or n > 100000:
        flag = 0
        break
    
    if n % 5 == 0:
        count += (n//5)
        break
    
    if (n - 5) % 2 == 0 :
        n -= 5
        count += 1
    elif n%2 == 0:
        n -= 2
        count += 1
    else:
        flag = 0
        break

    if n == 0:
        break

if flag:
    print(count)
else:
    print(-1)
     