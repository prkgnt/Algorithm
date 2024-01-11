def w(a, b, c):
    if dp[a][b][c] != -51:
        return dp[a][b][c]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20,20,20)
        return dp[a][b][c]
    elif a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


dp = [[[-51]*102 for _ in range(102)] for _ in range(102)]
res = []
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    res.append(f"w({a}, {b}, {c}) = {w(a,b,c)}")

for r in res:
    print(r)