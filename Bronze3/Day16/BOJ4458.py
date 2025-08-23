T = int(input())

for i in range(T):
    text = input()
    text = text[0].upper() + text[1:]  # string 값 잘 변경할 수 있는가?
    print(text)
