import sys

# input = sys.stdin.readline

A = int(input())
M = input()
B = int(input())

if M == "*":
    print(A * B)
else:
    print(A + B)
