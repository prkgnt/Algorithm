n = int(input())
arr = list(map(int, input().split()))
arr_reverse = arr[::-1]

# 증가하는 수열의 각 값들 저장
dp_increase = [0]*n
# 감소하는 값들의 각 값들 저장
dp_decrease = [0]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
        # 감소하는 경우 거꾸로 보면 결국 증가하는 수열임
        if arr_reverse[i] > arr_reverse[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

res = []
for i in range(n):
    # 증가하는 수 + 자기 자신 + 감소하는 수
    res.append(dp_increase[i] + 1 + dp_decrease[n-i-1])
print(max(res))