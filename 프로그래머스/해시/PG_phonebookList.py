# 아래 코드는 시간 초과
# def solution(phone_book):
#     answer = True
#     arr = []
#     idx = 0
    
#     for i in range(len(phone_book)):
#         arr.append(phone_book[i])
#     arr.sort(key=len)

#     while True:
#         if idx == len(arr):
#                 answer = True
#                 return answer
#         sliced_arr = [[element[:len(arr[idx])], element[len(arr[idx]):]] for element in arr]
#         phone_dict = {}
#         for element in sliced_arr:
#             key = element[0]
#             value = element[1] if len(element) > 1 else ''
#             if key in phone_dict:
#                 phone_dict[key].append(value)
#             else:
#                 phone_dict[key] = [value]
        
#         for i in range(len(phone_dict)):
#             if len(phone_dict.get(list(phone_dict.keys())[i])) > 1:
#                 answer = False
#                 return answer
#         idx += 1

# 정답 코드
def solution(phone_book):
    phone_book.sort() 
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True