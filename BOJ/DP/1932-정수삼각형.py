N = int(input())
arr = []
for i in range(N):
    x = list(map(int, input().split()))
    arr.append(x)

# dp[i][j] = i, j 번째 값에서 합의 최대값
dp = [[0] * N for _ in range(N)]
dp[0][0] = arr[0][0]
for i in range(1, N):
    for j in range(0, len(arr[i])):
        # dp = 오른쪽 위에서의 최대값과 왼쪽 위에서의 최대값 중 큰 값 + 현재 값
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

print(max(dp[N-1]))