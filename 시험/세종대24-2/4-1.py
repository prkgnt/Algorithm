# 4-1번
a,b,c = map(int, input().split())

for i in range(3):
    ac, bc, cc = 0, 0, 0
    same = 0
    candy = input()
    for j in range(6):
        if candy[j] == 'A':
            ac += 1
        elif candy[j] == 'B':
            bc += 1
        elif candy[j] == 'C':
            cc += 1
        if j >= 2:
            if candy[j-1] == candy[j] and candy[j-2] == candy[j]:
                same = 1
    if ac > a or bc > b or cc > c:
        print("Candy is not enough!")
    elif same == 1:
        print("Tired of candy!")
    else:
        print("Tastes good!")
