from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
init = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            init = [i, j]
            arr[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

queue = deque()


def target(w):
    visited = []
    # 먹을 수 있는 타겟 물고기 담는 배열
    t_arr = []
    # 이동 거리 저장 배열
    dist = [[1]*n for _ in range(n)]
    while queue:
        i, j = queue.popleft()
        visited.append([i, j])
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if [nx, ny] not in visited:
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] > w:
                        continue
                    else:
                        dist[nx][ny] = dist[i][j] + 1
                        if arr[nx][ny] == 0 or arr[nx][ny] == w:
                            queue.append([nx, ny])
                            visited.append([nx, ny])
                            continue
                        elif arr[nx][ny] < w:
                            t_arr.append([nx, ny, dist[nx][ny]])
    return t_arr


w = 2
queue.append(init)
now = init
res = 0
cnt = 0

while True:
    x = target(w)
    # 이동 시간 순으로 먼저 정렬 후, 가장 위에, 가장 왼쪽 우선 정렬
    x = sorted(x, key=lambda r: (r[2], r[0], r[1]))

    if x:
        # 가장 첫번째 원소 타겟으로 선택
        t = x[0]
        # 상어가 먹었으므로 0으로 설정
        arr[t[0]][t[1]] = 0
        # 큐에 남은거 모두 삭제 후 타겟으로 처음 위치 변경
        queue.clear()
        queue.append([t[0], t[1]])
        # 먹은 물고기 개수 1 추가
        cnt += 1
        if cnt == w:
            w += 1
            cnt = 0
        # 결과에 이동시간 - 1 (초기값이 1이라서 1 빼줌. 고치기 귀찮아서 그냥 1 뺌 ㅠ)
        res += t[2] - 1
        # 현재 위치 갱신
        now = [t[0], t[1]]
    else:
        break

print(res)