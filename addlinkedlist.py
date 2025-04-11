from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sd = defaultdict(int)
        left=right=0
        res=0
        while right<len(s):
            r=s[right]
            sd[r]+=1
            while sd[r]>1:
                l=s[left]
                sd[l]-=1
                left+=1
            res = max(res,right-left+1)
            right+=1
        return res

Sol = Solution()
print(Sol.lengthOfLongestSubstring("abcabcbb"))