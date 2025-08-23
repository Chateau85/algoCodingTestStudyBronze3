import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    sum = 0
    for _ in range(N):
        temp = int(input())
        sum += temp
    if sum == 0:
        print("0")
    elif sum > 0:
        print("+")
    else:
        print("-")
