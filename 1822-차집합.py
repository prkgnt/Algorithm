from collections import defaultdict
a, b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
res = []

dict = defaultdict(int)

for i in range(b):
    dict[arr_b[i]] = 1

for i in range(a):
    if dict[arr_a[i]] == 1:
        continue
    else:
        res.append(arr_a[i])

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i], end=" ")

