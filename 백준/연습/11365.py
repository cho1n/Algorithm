import sys
flag = 1

while True:
    
    S = list(sys.stdin.readline().rstrip())
    ans = ""
    
    if S[0] == 'E' and S[1] == 'N' and S[2] == 'D':
        sys.exit()
    
    for i in range(len(S)-1, -1, -1):
        ans += S[i]
    print(ans)

    