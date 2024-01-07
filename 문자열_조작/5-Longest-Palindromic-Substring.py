class Solution:
    # 내가 푼거
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for n in range(1, len(s)+1):
            for i in range(0, len(s)-n+1):
                x = s[i:i+n]
                if x[::-1] == x:
                    result = x
        return result

    # 책 풀이
    def sol(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    return s[left+1:right]
            return s[left+1:right]

        result = ""
        if len(s) < 2 or s[::-1] == s:
            return s

        for i in range(len(s)):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result


sol = Solution()
print(sol.sol("ccd"))