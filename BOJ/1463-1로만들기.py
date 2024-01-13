n = int(input())
# dp[i] = 1부터 i까지 필요한 계산의 최솟값
dp = [1000000] * (n+1)
dp[1] = 0
for i in range(1,n+1):
    # 더하기 연산을 했을 때
    if i+1 <= n and dp[i] + 1 < dp[i+1]:
        dp[i+1] = dp[i] + 1
    # *3 연산을 했을 때
    if i*3 <= n and dp[i] + 1 < dp[i*3]:
        dp[i*3] = dp[i] + 1
    # *2 연산을 했을 때
    if i*2 <= n and dp[i] + 1 < dp[i*2]:
        dp[i*2] = dp[i] + 1
print(dp[n])
