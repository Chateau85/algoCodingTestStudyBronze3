import sys

input = sys.stdin.readline

A = list(map(int, input().split()))
A.sort()
if A[2] >= A[0] + A[1]:
    A[2] = A[0] + A[1] - 1

print(sum(A))
