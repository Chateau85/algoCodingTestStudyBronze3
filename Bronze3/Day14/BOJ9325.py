T = int(input())
for i in range(T):
    amount = int(input())
    N = int(input())
    for j in range(N):
        item, price = map(int, input().split())
        amount += item * price
    print(amount)
