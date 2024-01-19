n = int(input())
li = list(map(int, input().split()))

# dp[i] = i번째까지의 합 중 가장 큰 합
dp = [-1001]*n
dp[0] = li[0]

for i in range(1, n):
    # 전까지의 최대값과 현재값의 합이 현재 값보다 크면 갱신
    if dp[i-1] + li[i] > li[i]:
        dp[i] = dp[i-1] + li[i]
    else:
        # 전까지의 최대값이 현재값보다 작으면 현재 값을 최대값으로 갱신
        dp[i] = li[i]

print(max(dp))