#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def matrixLand(A):
    # dp[i][j][0] = i,j에서 안밟았을 때 최댓값
    dp = [[[0]*2 for _ in range(m)] for _ in range(n)]
    queue = deque()
    dx = [0, 1, 0]
    dy = [1, 0, -1]
    queue.append([0, 0])
    dp[0][0][1] = A[0][0]
    dp[0][0][0] = A[0][0]
    while queue:
        i, j = queue.popleft()
        for d in range(3):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0<=nx<n and 0<=ny<m:
                # 밟고 왔을때
                if dp[nx][ny][1] < dp[i][j][1]:
                    dp[nx][ny][1] = dp[i][j][1]
                    queue.append([nx,ny])
                # 안밟고 와서 새로 밟을 때
                if dp[nx][ny][0] < dp[i][j][1] + A[nx][ny]:
                    dp[nx][ny][0] = dp[i][j][1] + A[nx][ny]
                    queue.append([nx,ny])
    for x in dp:
        print(x)
    print('------')
    for x in A:
        print(x)
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    A = []

    for _ in range(n):
        A.append(list(map(int, input().rstrip().split())))

    result = matrixLand(A)
    print(result)
