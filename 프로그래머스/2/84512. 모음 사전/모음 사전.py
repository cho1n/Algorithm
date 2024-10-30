def solution(word):
    global answer
    answer = 0
    alphabats = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(string):
        global answer
        answer += 1

        if string == word:
            return True

        if len(string) == 5:
            return False

        for alpha in alphabats:
            if dfs(string + alpha) == True:
                return True
    
    
    for alpha in alphabats:
        if dfs(alpha) == True:
            return answer