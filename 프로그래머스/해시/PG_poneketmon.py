def solution(nums):
    answer = 0
    N = len(nums)
    dic = {}
    for a in nums:
        dic[a] = a
    if len(dic) > (N/2):
        answer = N//2
    else :
        answer = len(dic)
        
    return answer

print(solution([3,2,3,1]))