n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# dp[i][0, 1] = i-1번째 잔을 마시고 난 후 i번째를 마셨을 때의 최댓값
#               i-2번째 잔을 마시고 난 후 i번째를 마셨을 때의 최댓값

def sol():
    res = 0
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = arr[0]
    dp[0][1] = arr[0]
    dp[1][0] = arr[0] + arr[1]
    dp[1][1] = arr[1]
    for i in range(2, n):
        dp[i][1] = max(map(max, dp[:i-1])) + arr[i]
        dp[i][0] = dp[i-1][1] + arr[i]

    #print(arr)
    #print(dp)
    return max(map(max,dp))

if n == 1:
    print(arr[0])
else:
    print(sol())
