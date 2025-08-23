ABC = list(map(int, input().split()))
ABC.sort()

order = input()
for i in order:
    if i == 'A':
        print(ABC[0], end=' ')
    elif i == 'B':
        print(ABC[1], end=' ')
    else:
        print(ABC[2], end=' ')
