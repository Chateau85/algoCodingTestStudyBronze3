N, W, H = map(int, input().split())
size = W * W + H * H

for _ in range(N):
    temp = int(input())
    now_size = temp * temp
    if size < now_size:
        print("NE")
    else:
        print("DA")
