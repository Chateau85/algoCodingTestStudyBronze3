import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
team = 0
while True:
    if N - 2 + M - 1 < K or N < 2 or M < 1:  # 인턴쉽에 참여할 학생보다 남은 학생 수가 적으면
        break

    if N >= 2 and M >= 1:
        team += 1
        N -= 2
        M -= 1

print(team)
