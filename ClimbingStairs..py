class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1 for i in range(n+2)]
        return self.Climb(n+1,dp)


    def Climb(self,ind,dp):
        if ind <= 0:return 0
        if ind == 1:return 1
        if dp[ind]!=-1:return dp[ind]
        dp[ind] = self.Climb(ind-1,dp) + self.Climb(ind-2,dp)
        return dp[ind]
        
