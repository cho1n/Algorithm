def solution(size):
    answer = []
    max1, max2 = 0, 0
    
    for i in range(len(size)):
        if size[i][0] < size[i][1]:
            size[i][0], size[i][1] = size[i][1], size[i][0]
        max1 = max(max1, size[i][0])
        max2 = max(max2, size[i][1])
    answer = max1 * max2    
            
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))