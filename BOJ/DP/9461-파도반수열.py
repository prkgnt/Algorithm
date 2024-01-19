T = int(input())
dp = [-1] * 101
for _ in range(T):
    N = int(input())
    if dp[N] != -1:
        print(dp[N])
        continue

    for i in range(1, N+1):
        if i <= 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-3]

    print(dp[N])