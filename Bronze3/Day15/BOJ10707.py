A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

A_amount = P * A
B_amount = B

if P > C:
    B_amount += (P - C) * D

print(min(A_amount, B_amount))
