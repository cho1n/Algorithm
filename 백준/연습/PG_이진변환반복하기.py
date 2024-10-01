answer = [1, 0]

def removeZero(x):
    words = []
    s = ""
    for l in x:
        words.append(l)
    
    while '0' in words:    
        words.remove('0')
        answer[1] += 1
        
    for i in words:
        s += i
    
    return s

def changeBinary(x):
    answer[0] += 1
    return bin(int(len(x)))[2:]

def solution(s):
    flag = 1
        
    while flag:
        s = removeZero(s)
        if len(s) == 1 and s == '1':
            break
        s= changeBinary(s)
        if len(s) == 1 and s == '1':
            break
        
    return answer

print(solution("1111111"))

def solution(s):
    answer = []
    times = 0
    s_num = 0

    while s != "1":
        s_num += s.count("0")
        s = s.replace("0", "")
        c = len(s)
        s = bin(int(c))[2:]
        times += 1

    answer.append(times)
    answer.append(s_num)

    return answer
