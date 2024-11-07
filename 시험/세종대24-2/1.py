# 1번
m = int(input())
n = int(input())
arr = [0]*n
res = 0
for i in range(n):
    arr[i] = int(input())
arr.sort(reverse=True)
x = 0
for i in range(n//m):
    res += min(arr[x:x+m]) * m
    x += m

print(res)