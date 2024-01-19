n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

# 전깃줄이 교차한다는 것은 arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1] 혹은 그 반대
# 전깃줄이 교차하지 않으려면 A를 오름차순으로 정렬 후 B가 증가하는 수열이여야 함
# 즉 A를 정렬 후 가장 긴 증가하는 수열을 찾은 뒤 n에서 뺴주면 됨
# 아이디어의 핵심은 교차하지 않는 경우를 찾는 것이 아닌 가장 많이 교차하는 경우를 찾는 것!
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
