n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = [0]*3

#y//3 <- 이런식으로 안헷갈리게 조심하기!
def sol(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                sol(x, y, n//3)
                sol(x+n//3, y, n//3)
                sol(x+2*(n//3), y, n//3)

                sol(x, y+n//3, n//3)
                sol(x+n//3, y+n//3, n//3)
                sol(x+2*(n//3), y+n//3, n//3)

                sol(x, y+2*(n//3), n//3)
                sol(x+n//3, y+2*(n//3), n//3)
                sol(x+2*(n//3), y+2*(n//3), n//3)
                return 1
    res[color+1] += 1

sol(0,0, n)
for r in res:
    print(r)