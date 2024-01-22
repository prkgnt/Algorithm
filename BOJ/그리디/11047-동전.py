N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
res = K
cnt = 0
for i in range(N-1, -1, -1):
    if res == 0:
        break
    if arr[i] <= res:
        cnt += res//arr[i]
        res = res % arr[i]
print(cnt)