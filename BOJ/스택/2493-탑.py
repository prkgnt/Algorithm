n = int(input())
li = list(map(int, input().split()))
res = [0] * n
stack = []
stack.insert(0, [li[n-1], n-1])
stack_len = 0
for i in range(n-2, -1, -1):
    if stack_len >= 0:
        if li[i] <= stack[stack_len][0]:
            stack.append([li[i], i])
            stack_len += 1
        else:
            while stack:
                if li[i] <= stack[stack_len][0]:
                    break
                else:
                    res[stack[stack_len][1]] = i+1
                    stack.pop()
                    stack_len -= 1
            stack.append([li[i], i])
            stack_len += 1
    else:
        stack.append([li[i], i])
        stack_len += 1

print(" ".join(map(str, res)))

