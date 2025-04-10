from typing import List


class Solution(object):
    def rankTeams(self, votes: List[str]) -> str:
        d={}
        for vote in votes:
            for i,char in enumerate(vote):
                if char not in d:
                    d[char] = [0]*len(vote)
                d[char][i] +=1
        voted_name = sorted(d.keys())
        return "".join(sorted(voted_name,key=d.get,reverse=True))

votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
sol = Solution()
print(sol.rankTeams(votes))