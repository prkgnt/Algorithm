def maxTrailing(arr):
    min = arr[0]
    diff = -1
    for i in range(1, len(arr)):
        if arr[i] > min:
            diff = max(diff, arr[i] - min)
        else:
            min = arr[i]
    return diff

if __name__ == '__main__':

    #arr_count = int(input().strip())

    arr = [2, 3, 10, 2, 4, 8 , 1]

    result = maxTrailing(arr)

    print(result)