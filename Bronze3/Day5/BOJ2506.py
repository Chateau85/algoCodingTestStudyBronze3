import sys

input = sys.stdin.readline

N = int(input())
sum = 0
count = 0
A = list(map(int, input().split()))
for i in range(N):

    if A[i] == 1:
        count += 1
        sum += count
    else:
        count = 0
print(sum)
