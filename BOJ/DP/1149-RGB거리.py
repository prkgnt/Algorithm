N = int(input())

arr = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())


# dp[i][0, 1, 2] = i번째에서 r, g, b를 칠했을 때의 각각의 최솟값
dp = [[0] * 3 for _ in range(N+1)]

# 모든 값을 계산하지만 전 과정에서 계산한 것을 이용하여 빠르게 계산
# 즉, 어떤 값만을 선택하여 최솟값을 도출하는 식같은건 없음
for i in range(1, N+1):
    # 현재 빨간색을 칠할 경우
    # 전 단계에서 초록색을 칠했을 때와 파란색을 칠했을 때의 최솟값을 비교 후
    # 그 중 작은 값 + 현재 빨간 색의 값
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

print(min(dp[N]))
