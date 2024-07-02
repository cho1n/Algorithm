def solution(clothes):
    answer = 1
    dic = {}
    keys = []
    
    for i in clothes:
        key = i[1]
        value = i[0]
        if key not in keys:    
            keys.append(key)
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
    
    for key in keys:
        answer *= (len(dic[key]) + 1) 

    return (answer - 1)


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))