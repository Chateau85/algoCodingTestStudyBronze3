import sys

input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break

    if max(A, B, C) >= A + B + C - max(A, B, C):
        print("Invalid")
    elif A == B == C:
        print("Equilateral")
    elif A == B or B == C or C == A:
        print("Isosceles")
    else:
        print("Scalene")
