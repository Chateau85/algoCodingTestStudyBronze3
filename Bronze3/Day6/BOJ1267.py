import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Y_amount = 0
M_amount = 0
for i in range(N):
    Y_amount += 10
    M_amount += 15
    time = A[i]

    Y_amount += time // 30 * 10
    M_amount += time // 60 * 15

if Y_amount == M_amount:
    print("Y M " + str(Y_amount))
elif Y_amount < M_amount:
    print("Y " + str(Y_amount))
else:
    print("M " + str(M_amount))
