import sys

input = sys.stdin.readline

S, C = map(int, input().strip().split())
L = []
remain = 0

for _ in range(S):
    L.append(int(input().strip()))

# L.sort()
# if S == C:
#     for i in range(1, len(L)):
#         remain += L[i] - L[i - 1]
#
#     print(remain)
#     exit(0)

# else:

start = 1
end = max(L)
cut = 0
while start <= end:
    mid = (start + end) // 2
    num = 0
    for length in L:
        num += length // mid

    if num >= C:
        cut = mid
        start = mid + 1

    else:
        end = mid -1

total = sum(L)
used = C * cut
print(total - used)
