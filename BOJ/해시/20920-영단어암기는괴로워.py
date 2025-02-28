n, m = map(int, input().split())
di = {}
for i in range(n):
    word = input()
    if len(word) < m:
        continue
    if word not in di:
        di[word] = 1
    else:
        di[word] += 1

res = [k for k, v in sorted(di.items(), key=lambda x: (x[1], len(x[0]), [-ord(c) for c in x[0]]), reverse=True)]

for x in res:
    print(x)