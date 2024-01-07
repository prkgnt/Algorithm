from typing import List
class Solution:
    # 브루트 포스 (내가 푼거)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 딕셔너리로 풀기
    def sol(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target-num in nums_map:
                # 자기 자신 조회하는 걸 방지
                if nums_map[target-num] != i:
                    return [nums_map[target-num], i]

sol = Solution()
print(sol.sol([3,3], 6))