from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ds=defaultdict(int)
        left=right=0
        pal=0
        while right<len(s):
            r=s[right]
            ds[r]+=1
            if right>1:
                l=s[left]
                if l == r[::-1]:
                    return s[left:right+1]
                left+=1
            right+=1
        return False

sol = Solution()
print(sol.longestPalindrome("cbbd"))