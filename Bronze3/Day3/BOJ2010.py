import sys

input = sys.stdin.readline

N = int(input())
Sum = 0
for i in range(N):
    Sum += int(input())

print(Sum - (N - 1))
