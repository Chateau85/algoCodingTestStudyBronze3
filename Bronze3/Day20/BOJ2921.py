N = int(input())

# 0 => 0
# 1 => 0, 1
# 2 => 0, 1, 2

sum = 0
for i in range(N + 1):
    for j in range(i + 1):
        sum += i
        sum += j

print(sum)
