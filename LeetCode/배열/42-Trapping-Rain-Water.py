from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = sum(height)
        for i in range(len(height)-1):
            # 현재 높이보다 다음 칸의 높이가 낮으면
            # 다음 칸을 웅덩이라 지칭, 현재 높이를 왼쪽 벽으로 지칭
            if height[i] > height[i+1]:
                for j in range(i+2, len(height)):
                    # 왼쪽 벽과 같거나 높은 곳(오른쪽 벽)이 있으면 왼쪽 벽 높이로 맞춤
                    if height[j] >= height[i]:
                        for x in range(i, j):
                            height[x] = height[i]
                        break
                    # 웅덩이보다 높은 곳이 있으면 웅덩이 높이로 맞춤
                    if height[j] > height[i+1]:
                        for x in range(i+1, j):
                            height[x] = height[j]

        return sum(height) - cnt

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,9,4,5,3,2]))