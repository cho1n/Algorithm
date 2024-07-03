list_1 = []
list_2 = []
dic = {}

N = int(input())
list_1 = set(map(int, input().split(' ')))
M = int(input())
list_2 = list(map(int, input().split(' ')))

com_set = (set(list_1) & set(list_2))

for i in list_2:
    if i in list_1:
        print(1)
    else:
        print(0)