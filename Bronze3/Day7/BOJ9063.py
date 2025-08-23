import sys

input = sys.stdin.readline

N = int(input())
minX, minY = map(int, input().split())
maxX = minX
maxY = minY
for i in range(N - 1):
    X, Y = map(int, input().split())
    if X > maxX: maxX = X
    if X < minX: minX = X
    if Y > maxY: maxY = Y
    if Y < minY: minY = Y

print((maxX - minX) * (maxY - minY))
