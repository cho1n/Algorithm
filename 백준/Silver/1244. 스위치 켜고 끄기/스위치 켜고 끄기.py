num = int(input())
switchs = list(map(int, input().split()))
students = int(input())

def man(x):
    temp = x
    
    if x <= len(switchs):
        
        if switchs[x-1] == 1:
            switchs[x-1] = 0
        else:
            switchs[x-1] = 1
    
    while True:
        x += temp
        if x > len(switchs):
            break
        else:
            if switchs[x-1] == 1:
                switchs[x-1] = 0
            else:
                switchs[x-1] = 1
            
def woman(x) :
    x -= 1
    i = 1
    
    if x <= len(switchs)-1:
        
        if x-i >= 0 and x+i < len(switchs):
            
            if switchs[x-i] != switchs[x+i]:
                if switchs[x] == 1:
                    switchs[x] = 0
                else:
                    switchs[x] = 1
                
            else:
                while True:
                    if (x-i) >= 0 and (x+i) < len(switchs):
                        if switchs[x-i] == switchs[x+i]:
                            i += 1
                        else:
                            i -= 1
                            break
                    else:
                        i -= 1
                        break
                        
                for j in range(x-i, x+i+1, 1):
                    if switchs[j] == 1:
                        switchs[j] = 0
                    else:
                        switchs[j] = 1
        else:
            if switchs[x] == 1:
                switchs[x] = 0
            else:
                switchs[x] = 1            

for _ in range(students):
    
    gender, switch = map(int, input().split())
    
    if gender == 1 :
        man(switch)
    else:
        woman(switch)


if len(switchs) <= 20:
    for i in range(len(switchs)):
        print(switchs[i], end=' ')
        
else:
    start = 0
    ends = 20
    flag = 1
    
    while True:
        
        for i in range(start, ends):
            print(switchs[i], end=' ')
            
        print()
            
        if ends == len(switchs):
            break
        
        start += 20
        ends += 20
        
        if ends >= len(switchs):
            ends = len(switchs)