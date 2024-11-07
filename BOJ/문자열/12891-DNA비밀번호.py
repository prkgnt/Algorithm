s, p = map(int,input().split())
dna = input()
A,C,G,T = map(int, input().split())
res = 0
table = [0,0,0,0]
# 길이만큼 검사 후 새로온 애랑 빠지는 애만 검사
for i in range(0, p):
    if dna[i] == 'A':
        table[0] += 1
    elif dna[i] == 'C':
        table[1] += 1
    elif dna[i] == 'G':
        table[2] += 1
    elif dna[i] == 'T':
        table[3] += 1

if table[0] >= A and table[1] >= C and table[2] >= G and table[3] >= T:
    res += 1

for i in range(p, s):
    if dna[i-p] == 'A':
        table[0] -= 1
    elif dna[i-p] == 'C':
        table[1] -= 1
    elif dna[i-p] == 'G':
        table[2] -= 1
    elif dna[i-p] == 'T':
        table[3] -= 1
    if dna[i] == 'A':
        table[0] += 1
    elif dna[i] == 'C':
        table[1] += 1
    elif dna[i] == 'G':
        table[2] += 1
    elif dna[i] == 'T':
        table[3] += 1
    if table[0] >= A and table[1] >= C and table[2] >= G and table[3] >= T:
        res += 1

print(res)