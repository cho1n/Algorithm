N = int(input())
peoples = []
tips = 0
tip = 0
for l in range(N):
    peoples.append(int(input()))
    
peoples.sort(reverse=True)

for i in range(len(peoples)):
    tip = peoples[i] - ((i+1) - 1)
    if tip > 0:
        tips += tip

print(tips)
