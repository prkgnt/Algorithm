# 개구림 다시 풀기
n = int(input())
arr = [0] * n
sum_arr = []
for i in range(n):
    arr[i] = int(input())
arr.sort()

for i in range(n):
    for j in range(n):
        # if i == j:
        #     continue
        sum_arr.append(arr[i]+arr[j])
sum_arr = list(set(sum_arr))
res = 0
for i in range(n-1, -1, -1):
    for j in range(n):
        if i == j:
            continue
        # print(arr[i], arr[i]-arr[j], arr[i]-arr[j] in sum_arr)
        if (arr[i] - arr[j]) in sum_arr:
            print(arr[i])
            # res = arr[i]
            exit()
# print(res)


