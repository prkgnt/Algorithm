n = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for i in range(n):
    for j in range(i+1):
        cnt += arr[j]

print(cnt)