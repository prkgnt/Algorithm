n = int(input())
x = int(input())
b = 8
res = 0

if 2 <= n <= 4:
    if x % 2 == 0:
        res += b * (x//2) + (n-1)
    if x % 2 != 0:
        res += b * (x // 2) + 1
        res += b - n
elif n == 5:
    res += b * x + 1
    res += 3
else:
    res += b * x
print(res)
