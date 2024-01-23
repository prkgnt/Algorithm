n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 회의가 끝나는 시간 순으로 정렬
# 만약 끝나는 시간이 같을 경우 회의 시작 순 정렬
# 3
# 4 4
# 3 4
# 2 4
# 위의 경우 생각하면 회의 시작 순 정렬 해야함
sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))

cnt = 1
last = sorted_arr[0][1]
# 회의가 끝나는 순으로 정렬 후 연속된 회의 개수 출력
# 어차피 회의 끝나는 시간은 무조건 시작시간보다 같거나 큼
# 이해 잘 안되니 외우기 ㅠ..
for i in range(1, n):
    if sorted_arr[i][0] >= last:
        cnt += 1
        last = sorted_arr[i][1]
print(cnt)