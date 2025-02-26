n = int(input())
dt = {}
dt["ChongChong"] = 1
for i in range(n):
    a, b = input().split()
    if a in dt or b in dt:
        dt[a] = 1
        dt[b] = 1

print(len(dt))