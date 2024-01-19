import sys
sys.setrecursionlimit(10**7)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0
# x, y = 시작점의 좌표
def sol(x, y, n):
    global white
    global blue
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                sol(x,y,n//2)
                sol(x+n//2, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y+n//2, n//2)
                return 1
    if color == 1:
        blue += 1
    else:
        white += 1

sol(0, 0, n)
print(white)
print(blue)