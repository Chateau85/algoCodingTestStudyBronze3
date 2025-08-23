import sys

input = sys.stdin.readline
N = int(input())

while True:
    now = int(input())
    if now == 0:
        break

    if now % N == 0:
        print(str(now) + " is a multiple of " + str(N) + ".")
    else:
        print(str(now) + " is NOT a multiple of " + str(N) + ".")
