import sys

input = sys.stdin.readline

n = int(input())
A = B = 100
for i in range(n):
    C, D = map(int, input().split())
    if C > D:
        B -= C
    elif D > C:
        A -= D

print(A)
print(B)
