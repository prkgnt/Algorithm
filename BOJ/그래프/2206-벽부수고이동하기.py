import copy
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
wall = []
for i, v in enumerate(arr):
    for j, x in enumerate(v):
        if x == 1:
            wall.append([i, j])

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


def sol():
    res = 1000001

    while wall:
        tmp_arr = copy.deepcopy(arr)
        i, j = wall.pop()
        tmp_arr[i][j] = 0
        x = bfs(tmp_arr)
        if x != 0:
            if res > x:
                res = x
    if res == 1000001:
        print(-1)
    else:
        print(res)


def bfs(arr):
    dist = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([0, 0])
    dist[0][0] = 1
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[i][j] + 1
                    visited[nx][ny] = 1
    return dist[n-1][m-1]

sol()