dict = {}

def solution(clothes):
    for clothe in clothes:
        print(clothe)
        if clothe in dict:
            dict[clothe[1]] += 1
        else:
            dict[clothe[1]] = 1
    
    print(dict)

solution()