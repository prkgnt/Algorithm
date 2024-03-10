#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#
import numpy as np

def dfs(i, j, visitedNode, n):
    visitedNode.append([i, j])
    if i < n-1 and grid1[i+1][j] == '1':
        if [i+1, j] not in visitedNode:
            dfs(i+1, j, visitedNode, n)

    if i > 0 and grid1[i-1][j] == '1':
        if [i-1, j] not in visitedNode:
            dfs(i-1, j, visitedNode, n)

    if j < n-1 and grid1[i][j+1] == '1':
        if [i, j+1] not in visitedNode:
            dfs(i, j+1, visitedNode, n)

    if j > 0 and grid1[i][j-1] == '1':
        if [i, j-1] not in visitedNode:
            dfs(i, j-1, visitedNode, n)

    return visitedNode

def dfs2(i, j, visitedNode, n):
    visitedNode.append([i, j])
    if i < n-1 and grid2[i+1][j] == '1':
        if [i+1, j] not in visitedNode:
            dfs2(i+1, j, visitedNode, n)

    if i > 0 and grid2[i-1][j] == '1':
        if [i-1, j] not in visitedNode:
            dfs2(i-1, j, visitedNode, n)

    if j < n-1 and grid2[i][j+1] == '1':
        if [i, j+1] not in visitedNode:
            dfs2(i, j+1, visitedNode, n)

    if j > 0 and grid2[i][j-1] == '1':
        if [i, j-1] not in visitedNode:
            dfs2(i, j-1, visitedNode, n)

    return visitedNode

def countMatches(grid1, grid2):
    res = 0
    visited = []
    cnt = 0
    for i in range(0, len(grid1)):
        for j in range(0, len(grid1)):
            if grid1[i][j] == '1' and [i, j] not in visited:
                arr = dfs(i, j, [], len(grid1))
                visited.extend(arr)
                if grid2[i][j] == '1':
                    arr2 = dfs2(i, j, [], len(grid2))
                f = 1
                #print(arr, arr2)

                if len(arr) == len(arr2):
                    #print(arr2)
                    arr.sort()
                    arr2.sort()
                    for k in range(len(arr)):
                        if arr[k] != arr2[k]:
                            f = 0
                    if f == 1:
                        res += 1

    return res


grid1_count = int(input().strip())

grid1 = []

for _ in range(grid1_count):
    grid1_item = input()
    grid1.append(grid1_item)

grid2_count = int(input().strip())

grid2 = []

for _ in range(grid2_count):
    grid2_item = input()
    grid2.append(grid2_item)

result = countMatches(grid1, grid2)
print(result)