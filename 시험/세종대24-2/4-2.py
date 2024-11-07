# 못품

n,m,l = map(int, input().split())
res = 0
def recursive(before, now, i, ca, cb, cc):
    if i == 6:
        return 1
    if before == now:
        if before == 'A':
            if cb < m:
                return recursive(now, 'B', i+1, ca, cb+1, cc)
            if cc < m:
                return recursive(now, 'C', i + 1, ca, cb, cc+1)
        if before == 'B':
            if ca < m:
                return recursive(now, 'A', i+1, ca+1, cb, cc)
            if cc < m:
                return recursive(now, 'C', i + 1, ca, cb, cc+1)
        if before == 'C':
            if cb < m:
                return recursive(now, 'B', i+1, ca, cb+1, cc)
            if ca < m:
                return recursive(now, 'A', i + 1, ca+1, cb, cc)
    else:
        if ca < m:
            return recursive(now, 'A', i + 1, ca + 1, cb, cc)
        if cb < m:
            return recursive(now, 'B', i + 1, ca, cb + 1, cc)
        if cc < m:
            return recursive(now, 'C', i + 1, ca, cb, cc + 1)


if n > 0:
    if n > 1:
        res += recursive('A', 'A', 1, 2,0,0)
    if m > 0:
        res += recursive('A', 'B', 1, 1, 1, 0)
    if l > 0:
        res += recursive('A', 'C', 1, 1, 0, 1)
if m > 0:
    if n > 0:
        res += recursive('B', 'A', 1, 1, 1, 0)
    if m > 1:
        res += recursive('B', 'B', 1, 2, 0, 0)
    if l > 0:
        res += recursive('B', 'C', 1, 0, 1, 1)
if l > 0:
    if n > 0:
        res += recursive('C', 'A', 1, 1, 0, 1)
    if m > 1:
        res += recursive('C', 'B', 1, 0, 1, 1)
    if l > 0:
        res += recursive('C', 'C', 1, 0, 0, 2)

print(res)
