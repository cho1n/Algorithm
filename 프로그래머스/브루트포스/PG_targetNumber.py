def solution(numbers, target):
    answer = [0]
    
    def dfs(nums, current_sum, target):
        if not nums:
            if current_sum == target:
                answer[0] += 1
            return
        
        dfs(nums[1:], current_sum + nums[0], target)
        dfs(nums[1:], current_sum - nums[0], target)
        print(current_sum)
    
    dfs(numbers, 0, target)
    return answer

print(solution([1,1,1,1,1], 3))
