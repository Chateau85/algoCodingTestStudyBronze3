N = int(input())
data = list(input())

A = B = 0
for i in range(N):
    if data[i] == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")
