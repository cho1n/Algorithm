def sol(A, B):
    answer = ''
    temp = 0
    dic = {}
    for a in A:
        dic[hash(a)] = a
        temp += int(hash(a))
    for b in B:
        temp -= hash(b)
    answer = dic[temp]
    
    return answer

print(sol(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))