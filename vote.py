class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        votesnum={}
        for vote in votes:
            votesum[vote]=votesum.get(vote,0)+1
            votesum