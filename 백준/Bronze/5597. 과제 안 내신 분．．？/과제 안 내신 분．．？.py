students = [False] * 31

for _ in range(28):
   student = int(input())
   students[student] = True 

for i in range(1, len(students)):
    if students[i] == False:
        print(i)