class Solution(object):
    def twoSum(self, nums, target):
        indexnum={}
        for i in range(len(nums)):
            indexnum[nums[i]]=i
        for i in range(len(nums)):
            secondnum=target-nums[i]
            if secondnum in indexnum and indexnum[secondnum]!=i:
                return i, indexnum[secondnum]
        return []
    
nums=[3,3]
target=6
sol = Solution()
print(sol.twoSum(nums, target))
