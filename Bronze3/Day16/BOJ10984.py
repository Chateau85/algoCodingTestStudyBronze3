T = int(input())
for i in range(T):
    N = int(input())
    credits = 0
    sum = 0
    for j in range(N):
        A, B = map(float, input().split())
        credits += A
        sum += A * B
    avg = sum / credits
    print(int(credits), '%.1f' % avg)
