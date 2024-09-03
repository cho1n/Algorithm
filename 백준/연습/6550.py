import sys

while True:
    try:
        s, t = input().split()
        idx = 0
        
        for i in range(len(t)):
            if idx < len(s) and s[idx] == t[i]: idx += 1
        
        if idx == len(s):
            print("Yes")
        else:
            print("No")
        
    except:
        break
