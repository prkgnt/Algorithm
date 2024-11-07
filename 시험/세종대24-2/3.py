# 3번
n = int(input())
arr = list(map(int, input().split()))

main = []
sub = []
main_len = n-1
sub_len = -1
res = 0
for i in range(n-1, -1, -1):
    main.append(i+1)

for i in range(n):
    while True:
        if main_len == -1:
            break
        if main_len >= 0:
            if arr[i] == main[main_len]:
                main_len -= 1
                res += 1
                break
        if sub_len >= 0:
            if arr[i] == sub[sub_len]:
                sub.pop()
                sub_len -= 1
                res += 1
                break

        sub.append(main[main_len])
        main.pop()
        sub_len += 1
        main_len -= 1
print(res)
