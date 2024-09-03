import sys

dic = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 3,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 3,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 2,
    "X": 2,
    "Y": 2,
    "Z": 1
}

S = list(sys.stdin.readline().rstrip())
sum = 0

for i in S:
    sum += dic.get(i)
    if sum > 10:
        sum %= 10

if sum % 2 != 0 : print("I'm a winner!")
else: print("You're the winner?")