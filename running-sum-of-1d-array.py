class Solution(object):
    def runningSum(self, nums):
        if(len(nums)<=1000 and len(nums)>=1):
            retnums=[]
            prev=0
            for num in nums:
                if num>(-10**6) and num<= 10**6:
                    prev = prev + num
                    retnums.append(prev)
        return retnums
retnum=Solution().runningSum([1,2,3])
print(retnum)
