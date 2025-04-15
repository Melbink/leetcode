
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr_num=[]
        nums=sorted(nums)
        for num in nums:
            arr_num.append(num) if num not in arr_num else arr_num
        nums.clear()
        nums[:]=arr_num 
        return len(arr_num)


sol = Solution()
nums=[1,1,2]
print(sol.removeDuplicates(nums))
print(nums)