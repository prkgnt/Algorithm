n = int(input())
li = list(map(int, input().split()))

# dp[i] = i번째까지의 합 중 가장 큰 합
dp = [-1001]*n
dp[0] = li[0]
# 전체 합이 0보다 작지않으면 계속 갱신하면서 나아가기
# 전까지의 최대값과 현재값의 합이 현재 값보다 크면 갱신
for i in range(1, n):
    if dp[i-1] + li[i] > li[i]:
        dp[i] = dp[i-1] + li[i]
    else:
        dp[i] = li[i]


max = max(dp)

print(max)