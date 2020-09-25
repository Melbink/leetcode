class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [candies[i]+extraCandies>=max(candies) for i in range(len(candies))]


retcan=Solution().kidsWithCandies([1,2,3,4,5],3)

print(retcan)
