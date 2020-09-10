class Solution:
    def twoSum(nums, target):
        hash={}
        counter = len(nums)
        for i in range(counter):
            nimus=target-nums[i]
            if nimus in hash.keys():
                j=hash[nimus]
                return [i,j]
            else:
                hash[nums[i]]=i
        return []
valu=Solution.twoSum([1,2,3,4,5],8)
print(valu)