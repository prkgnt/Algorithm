def largestSubgrid(grid, maxSum):
    def is_valid(pSum, size, maxSum):
        n = len(pSum) - 1
        for i in range(size, n+1):
            for j in range(size, n+1):
                sub_sum = (pSum[i][j] - pSum[i - size][j]
                           - pSum[i][j - size] + pSum[i - size][j - size])
                if sub_sum > maxSum:
                    return False
        return True

    n = len(grid)
    pSum = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            pSum[i][j] = (pSum[i - 1][j] + pSum[i][j - 1] - pSum[i - 1][j - 1] +
                          grid[i - 1][j - 1])

    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if is_valid(pSum, mid, maxSum):
            left = mid + 1
        else:
            right = mid - 1

    return right





# 예시 테스트
grid = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

print(largestSubgrid(grid, 4))  # 출력: 1
print(largestSubgrid(grid, 14))  # 출력: 2
print(largestSubgrid(grid, 27))  # 출력: 3
print(largestSubgrid(grid, 3))  # 출력: 0