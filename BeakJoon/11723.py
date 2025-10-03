import sys

input = sys.stdin.readline

line = int(input().strip())
S = 0b000000000000000000000
output = []

for i in range(line):
    operator = input().strip().split()

    if operator[0] == "add":
        S |= (1 << int(operator[1]))
    elif operator[0] == "remove":
        S &= ~(1 << int(operator[1]))
    elif operator[0] == "check":
        if S & (1 << int(operator[1])) != 0:
            print(1)
        else:
            print(0)
    elif operator[0] == "toggle":
        S ^= (1 << int(operator[1]))
    elif operator[0] == "all":
        S = (1 << 21) - 1
    elif operator[0] == "empty":
        S = 0