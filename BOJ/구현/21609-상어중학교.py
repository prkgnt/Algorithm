import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def find_group(i, j, visited, target):
    visited.append((i, j))
    for d in range(4):
        nx = i+dx[d]
        ny = j+dy[d]
        if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == target or arr[nx][ny] == 0:
                find_group(nx, ny, visited, target)
    return visited

def find_biggest_group():
    visited = []
    max_len = 0
    max_rainbow = 0
    biggest_group = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and arr[i][j] > 0:
                group = find_group(i, j, [], arr[i][j])
                rainbow = 0
                for v in group:
                    if arr[v[0]][v[1]] == 0:
                        rainbow += 1
                    visited.append(v)

                if len(group) > max_len:
                    biggest_group = copy.deepcopy(group)
                    max_len = len(group)
                    max_rainbow = rainbow
                elif len(group) == max_len and max_rainbow < rainbow:
                    biggest_group = copy.deepcopy(group)
                    max_len = len(group)
                    max_rainbow = rainbow
                elif len(group) == max_len and max_rainbow == rainbow:
                    biggest_group = copy.deepcopy(group)
                    max_len = len(group)
                    max_rainbow = rainbow

    return biggest_group


def gravity():
    for i in range(n-1, -1, -1):
        for j in range(n):
            if arr[i][j] == -2:
                for k in range(i-1, -1, -1):
                    if arr[k][j] == -1:
                        break
                    if arr[k][j] >= 0:
                        arr[i][j] = arr[k][j]
                        arr[k][j] = -2
                        break



def rotate():
    rotated_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_arr[n-j-1][i] = arr[i][j]
    for i in range(n):
        for j in range(n):
            arr[i][j] = rotated_arr[i][j]



score = 0
while True:
    biggest_group = find_biggest_group()
    if len(biggest_group) < 2:
        break
    score += len(biggest_group)**2

    # 블록 제거
    for v in biggest_group:
        # print(arr[v[0]][v[1]], end=' ')
        arr[v[0]][v[1]] = -2
    # print(" ")
    # for i in range(n):
    #     print(arr[i])
    # print(" ")
    gravity()
    rotate()
    gravity()
    # for i in range(n):
    #     print(arr[i])
    # print("--------------------------")

print(score)






