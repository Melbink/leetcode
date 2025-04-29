class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        sum=0
        sorted_array=sorted(nums)
        len_sort=len(sorted_array)
        i = 0
        while i<len_sort:
            if ((sorted_array[i]+sorted_array[-1])>upper):
                sorted_array=sorted_array[:-1]
                len_sort=len(sorted_array)
                j=i+1
                while(j<len(sorted_array)):
                    if(i>=0 and (nums[i]+nums[j]>=lower) and (nums[i]+nums[j]<=upper)):
                        sum+=1
                    j=j+1
            elif (sorted_array[i]+sorted_array[0]<lower):
                sorted_array=sorted_array[1:]
                len_sort=len(sorted_array)
                j=i+1
                while(j<len(sorted_array)):
                    if(i>=0 and (nums[i]+nums[j]>=lower) and (nums[i]+nums[j]<=upper)):
                        sum+=1
                    j=j+1
            i+=1
        return sum

        

sol=Solution()
sol.countFairPairs([0,1,4,4,5,7],3,6)