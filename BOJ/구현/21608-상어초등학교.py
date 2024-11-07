n = int(input())
student = {}
res = 0
class_map = [[0]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n**2):
    num, a, b, c, d = map(int, input().split())
    student[num] = [a, b, c, d]

for num in student.keys():
    # score[0], [1], 위치
    max_score = [0, 0, -1, -1]
    # j행 k열
    for j in range(n):
        for k in range(n):
            # score[0] = 좋은 학생 개수, score[1] = 빈칸 개수
            score = [0, 0]

            if class_map[j][k] == 0:
                # 처음 만나는 빈 칸이면 저장 하기
                if max_score[2] == -1 and max_score[3] == -1:
                    max_score[2] = j
                    max_score[3] = k
                for d in range(4):
                    if 0 <= j+dx[d] < n and 0 <= k+dy[d] < n:
                        if class_map[j+dx[d]][k+dy[d]] == 0:
                            score[1] += 1
                        elif class_map[j+dx[d]][k+dy[d]] in student[num]:
                            score[0] += 1
                # 좋은 사람 주위에 많으면
                if max_score[0] < score[0]:
                    max_score[0] = score[0]
                    max_score[1] = score[1]
                    max_score[2] = j
                    max_score[3] = k
                # 빈칸 많으면 (같으면 그 전꺼로 유지. 0부터 올라가니까 3번 항목 만족)
                elif max_score[0] == score[0] and max_score[1] < score[1]:
                    max_score[0] = score[0]
                    max_score[1] = score[1]
                    max_score[2] = j
                    max_score[3] = k

    class_map[max_score[2]][max_score[3]] = num

for j in range(n):
    for k in range(n):
        tmp = 0
        for d in range(4):
            if 0 <= j + dx[d] < n and 0 <= k + dy[d] < n:
                if class_map[j + dx[d]][k + dy[d]] in student[class_map[j][k]]:
                    tmp += 1
        if tmp != 0:
            res += 10 ** (tmp-1)

print(res)

