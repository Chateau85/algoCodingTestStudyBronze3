import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    Y_sum = 0
    K_sum = 0
    for j in range(9):
        Y, K = map(int, input().split())
        Y_sum += Y
        K_sum += K

    if Y_sum > K_sum:
        print("Yonsei")
    elif K_sum > Y_sum:
        print("Korea")
    else:
        print("Draw")
