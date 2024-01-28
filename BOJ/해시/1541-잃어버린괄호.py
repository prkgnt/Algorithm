n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
dict = {}
for x in arr_m:
    if x in dict:
        print(dict[x])
    else:
        if x in arr:
            print(1)
            dict[x] = 1
        else:
            print(0)
            dict[x] = 0