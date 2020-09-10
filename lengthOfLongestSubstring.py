class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=1
        substr=""
        for i in range(len(s)):
            if not(s[i] in substr):
                substr=substr+s[i]
                y=s[i+1::]
                strtocheck=y[:count:]
                if not(substr in strtocheck):
                    count=count+1
                else:
                    break
            else:
                substr=s[i]

        return count
ret=Solution().lengthOfLongestSubstring("pwwkew")
print(ret)