T = int(input())

for i in range(T):
    A = list(map(int, input().split()))
    sum = 0
    min_val = 101
    for j in range(7):
        if A[j] % 2 == 0:  # 짝수일 때
            sum += A[j]  # 변수에 더해주기
            if min_val > A[j]:  # 최소값 업데이트
                min_val = A[j]

    print(str(sum) + " " + str(min_val))
