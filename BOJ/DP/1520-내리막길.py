
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dp = [[-1]*m for _ in range(n)]
def dfs(i, j):
    cnt = 0
    if i == n-1 and j == m-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[i][j]:
                cnt += dfs(nx, ny)
                dp[i][j] = cnt
    return cnt


res = dfs(0,0)
print(res)
# for x in dp:
#     print(x)