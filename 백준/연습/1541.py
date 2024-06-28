import sys

mathLine = sys.stdin.readline().strip()

arr = mathLine.split('-')

result = sum(map(int, arr[0].split('+')))

for expression in arr[1:]:
    result -= sum(map(int, expression.split('+')))

print(result)