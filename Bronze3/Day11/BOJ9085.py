import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    sum = 0
    for j in range(N):
        sum += temp[j]
    print(sum)
