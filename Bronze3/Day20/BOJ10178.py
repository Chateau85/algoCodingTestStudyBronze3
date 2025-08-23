T = int(input())

for _ in range(T):
    c, v = map(int, input().split())
    m = c // v
    n = c % v
    print("You get " + str(m) + " piece(s) and your dad gets " + str(n) + " piece(s).")
