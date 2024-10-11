from itertools import permutations

def check(perm, A):
    for i in range(len(A)):
        if A[i] == '<' and perm[i] > perm[i+1]:
            return False
        if A[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True

k = int(input())
A = input().split()

nums = [i for i in range(10)]
perms = permutations(nums, k+1)

min_ans = None
max_ans = None

for perm in perms:
    if check(perm, A):
        num_str = ''.join(map(str, perm))
        if min_ans is None or num_str < min_ans:
            min_ans = num_str
        if max_ans is None or num_str > max_ans:
            max_ans = num_str

print(max_ans)
print(min_ans)