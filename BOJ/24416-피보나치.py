n = int(input())

cnt = 1

def fibo(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    else:
        cnt += 1
        return fibo(n-1) + fibo(n-2)

def fibo_dp(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
fibo(n)
print(cnt, n-2)