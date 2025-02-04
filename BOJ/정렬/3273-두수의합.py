n = int(input())
arr = list(map(int, input().split()))
x = int(input())
res = 0
arr.sort()
# print(arr)
i=0
j=n-1
while True:
    if i >= j:
        break
    if arr[i] + arr[j] > x:
        j -= 1
    elif arr[i] + arr[j] < x:
        i += 1
    else:
        res += 1
        j -= 1

print(res)

#[1, 2, 3, 5, 7, 9, 10, 11, 12]