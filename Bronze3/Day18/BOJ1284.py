# 0은 4cm, 1은 2cm, 나머지 3cm
size = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    num = input()
    if int(num) == 0:
        break

    sum = len(num) + 1
    for i in num:
        index = int(i)
        sum += size[index]

    print(sum)
