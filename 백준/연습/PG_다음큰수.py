def solution(n):
    answer = 0
    n_binary = 0
    find_binary = n + 1
    find_count = 0
    bic_count = 0
    
    n_binary = format(n, 'b')
    bic_count = n_binary.count("1")
    
    while True:
        answer = format(find_binary, 'b')
        find_count = answer.count("1")
        if find_count == bic_count:
            return find_binary
        else:
            find_binary += 1
        
print(solution(15))