from  typing import List
class Solution:
    # 내 풀이 (브루트 포스) -> 타임아웃 ㅠ
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_map = {}
        nums.sort()

        for i, num in enumerate(nums):
            sum_map[num] = i

        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                x = -nums[i]-nums[j]

                if x in sum_map and sum_map[x] != i and sum_map[x] != j:
                    result = [nums[i], nums[j], x]
                    result.sort()

                    if result not in results:
                        results.append(result)
        return results


    # 책 풀이
    def sol(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == nums[i-1] and i>0:
                continue
            left = i + 1
            right = len(nums) - 1
            while right > left:
                if num + nums[left] + nums[right] > 0:
                    right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    results.append([num, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
sol = Solution()
print(sol.sol([-1,0,1,2,-1,-4]))
print(sol.sol([0,0,0,0]))

