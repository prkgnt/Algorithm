n = int(input())
arr = list(map(int, input().split()))
arr_reverse = arr[::-1]
#print(arr_reverse)

dp_increase = [0]*n
dp_decrease = [0]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
        if arr_reverse[i] > arr_reverse[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

# print(dp_increase)
# print(dp_decrease)
res = []
for i in range(n):
    res.append(dp_increase[i] + dp_decrease[n-i-1])
print(max(res) + 1)