class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        listnum={}
        listnum['I']=1
        listnum['V']=5
        listnum['X']=10
        listnum['L']=50
        listnum['C']=100
        listnum['D']=500
        listnum['M']=1000
        num=0
        for i in range(len(s)):
            if i>0 and listnum[s[i]]>listnum[s[i-1]]:
                num=(num + listnum[s[i]]-2*listnum[s[i-1]])
            else :
                num=(num + listnum[s[i]])
        return num
print(Solution().romanToInt("IV"))