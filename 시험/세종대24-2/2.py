# 2번
n = int(input())

res = 0
for i in range(1, n-1):
    r = 1
    while True:
        f = 0
        temp = i
        for j in range(2):
            temp += r
            if temp > n:
                f = 1
                break
        if f == 0:
            res += 1
            r += 1
        else:
            break

print(res)