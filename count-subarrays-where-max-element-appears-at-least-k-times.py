class Solution(object):
    def countSubarrays(self, nums, k):
        maxarr={}
        for i in range(len(nums)):
            maxarr[nums[i]]=maxarr.get(nums[i],0)+1
        sorted(maxarr.items(), key=lambda x: x[1], reverse=True)
        print(list(maxarr.items())[0])


sol=Solution()
sol.countSubarrays([1,1,3,4,5], 3)
