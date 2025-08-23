A, B, C = map(int, input().split())

range1 = B - A - 1
range2 = C - B - 1

print(max(range1, range2))
