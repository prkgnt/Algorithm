from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for str in strs:
            x = ''.join(sorted(str))
            if x in results:
                results[x].append(str)
            else:
                results[x] = [str]

        return list(results.values())


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
