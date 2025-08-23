import sys

input = sys.stdin.readline

N = int(input())
A = [0, 1, 0, 0]
for i in range(N):
    X, Y = map(int, input().split())
    temp = A[X]
    A[X] = A[Y]
    A[Y] = temp

for i in range(1, 4):
    if A[i] == 1:
        print(i)
        break
