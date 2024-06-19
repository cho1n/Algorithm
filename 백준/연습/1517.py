import sys
input = sys.stdin.readline
result = 0

def merge_sort(s, e) :
    global result
    if e-s < 1:
        return
    m = int(s+(e-s)/2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = arr[i]
    
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e :
        if tmp[index1] > tmp[index2] :
            arr[k] = tmp[index2]
            result = result + index2 - k #swap count
            k += 1
            index2 += 1
        else :
            arr[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        arr[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        arr[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
tmp = [0] * (N+1)
merge_sort(1, N)
print(result)