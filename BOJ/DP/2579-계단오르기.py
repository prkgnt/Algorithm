n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


def sol():
    # dp[i][j] = i번째 계단에서 전 계단을 밟고 올라온 최댓값, 전전 계단을 밟고 올라온 최댓값
    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = arr[0]
    dp[0][1] = arr[0]
    dp[1][0] = arr[0] + arr[1]
    dp[1][1] = arr[1]

    for i in range(2, n):
        # i단계에서 전(i-1) 계단을 밟고 올라올 시
        # i-1 단계에서 전전계단을 밟고 올라온 최댓값만 선택 가능
        dp[i][0] = dp[i - 1][1] + arr[i]
        # i단계에서 전전(i-2) 계단을 밟고 올라올 시
        # i-2 단계에서 어떤 계단을 밟고 올라오든 상관 없음
        dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + arr[i]

    # max(dp)가 아닌 마지막 계단의 최댓값 선택 (무조건 마지막 계단을 밟아야 하므로)
    return max(dp[n-1])


if n == 1:
    print(arr[0])
else:
    print(sol())
