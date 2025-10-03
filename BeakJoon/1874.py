import sys

input = sys.stdin.readline

n = int(input().strip())
target = []

for _ in range(n):
    target.append(int(input().strip()))

stack = []
operation = []
cur = 0

is_True = True

for x in target:
    while cur < x:
        cur += 1
        stack.append(cur)
        operation.append('+')

    if stack and stack[-1] == x:
        stack.pop()
        operation.append('-')
    else:
        is_True = False
        break

if is_True:
    print("\n".join(operation))

else:
    print("NO")