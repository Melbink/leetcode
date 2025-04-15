class Solution(object):
    def goodTriplets(self, nums1, nums2):
        count=0
        for i,j in zip(nums1, nums2):
            j= i+1
            while(j<len(nums2)):
                k= j+1
                while(k<len(nums2)):
                    if (nums1[i] < nums1[j] < nums1[k]) and (nums2[i] < nums2[j] < nums2[k]):
                        count+=1
                    k+=1
                j+=1
        return count
        
nums1 = [4,0,1,3,2]
nums2 = [4,1,0,2,3]
sol = Solution()
print(sol.goodTriplets(nums1, nums2))