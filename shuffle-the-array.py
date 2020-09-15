class Solution:
    def shuffle(self, nums, n):
        pairs = [(nums[i], nums[i+n]) for i in range(n)]
        return [pair[i] for pair in pairs for i in range(2)]
retnum=Solution().shuffle([1,2,3,4,5,6],3)
print(retnum)
