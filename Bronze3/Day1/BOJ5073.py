# 코딩테스트에서 데이터가 많을 때 사용하면 시간초과가 나는 경우가 있음
# input()
# print() => 줄바꿈이 이루어짐

import sys # 빠름
# sys.stdin.readline
# sys.stdout.write => 줄바꿈이 없음, str 값만 찍을 수 있음

input = sys.stdin.readline()

a = sys.stdin.readline()
print(a)
print(a)
print(a)
print(a)
