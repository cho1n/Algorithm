N = int(input())
count = 0
countList = []

graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    global count
    
    if x<= -1 or x>= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
if N <= 25 and N >= 5:
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True :
                countList.append(count)
                count = 0
                result += 1
            
print(result)
countList.sort()
for i in range(len(countList)):
    print(countList[i])