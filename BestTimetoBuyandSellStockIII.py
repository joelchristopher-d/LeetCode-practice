class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cap=2
        dp=[[[0 for i in range(cap+1)] for j in range(2)] for k in range(len(prices)+1)]
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(0,2,1):
                for k in range(1,cap+1,1):
                    if buy:
                        dp[ind][buy][k] = max(-prices[ind]+dp[ind+1][0][k],0+dp[ind+1][1][k])
                    else:
                        dp[ind][buy][k] = max(prices[ind]+dp[ind+1][1][k-1],0+dp[ind+1][0][k])
        return dp[0][1][2]



        cap=2
        dp=[[[-1 for i in range(cap+1)] for j in range(2)] for k in range(len(prices))]
        return self.buysell(prices,0,1,len(prices),dp,cap)

    def buysell(self,prices,ind,buy,n,dp,cap):
        if ind == n:return 0
        if cap==0:return 0
        if dp[ind][buy][cap]!=-1:return dp[ind][buy][cap]
        if buy:
            dp[ind][buy][cap] = max(-prices[ind]+self.buysell(prices,ind+1,0,n,dp,cap),0+self.buysell(prices,ind+1,1,n,dp,cap))
            return dp[ind][buy][cap]
        else:
            dp[ind][buy][cap] = max(prices[ind]+self.buysell(prices,ind+1,1,n,dp,cap-1),0+self.buysell(prices,ind+1,0,n,dp,cap))
            return dp[ind][buy][cap]
