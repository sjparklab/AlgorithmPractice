import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

address_pw = dict()

for _ in range(N):
    address, password = input().strip().split()
    address_pw[address] = password

for _ in range(M):
    print(address_pw[input().strip()])