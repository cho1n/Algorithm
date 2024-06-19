def solution(answers):
    answer = []
    
    first_answer = [1,2,3,4,5]
    second_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    third_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3, max_num = 0, 0, 0, 0
    
    for i in range(len(answers)) :
        if first_answer[i%5] == answers[i]:
            cnt1 += 1
        if second_answer[i%8] == answers[i]:
            cnt2 += 1
        if third_answer[i%10] == answers[i]:
            cnt3 += 1
                
    max_num = max(cnt1, cnt2, cnt3)
    if max_num == cnt1:
        answer.append(1)
    if max_num == cnt2:
        answer.append(2)
    if max_num == cnt3:
        answer.append(3)
    
    return answer