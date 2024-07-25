class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1 for i in range(2)] for i in range(len(prices)+1)]
        dp[len(prices)][0]=dp[len(prices)][1]=0
        for i in range(len(prices)-1,-1,-1):
            for j in range(0,2,1):
                profit = 0
                if j:
                    profit = max(-prices[i]+dp[i+1][0],0+dp[i+1][1])
                else:
                    profit = max(prices[i]+dp[i+1][1],0+dp[i+1][0])
                dp[i][j]=profit
        return dp[0][1]

        dp=[[-1 for i in range(2)] for i in range(len(prices))]
        return self.buysell(prices,0,1,len(prices),dp)

    def buysell(self,prices,ind,buy,n,dp):
        if ind == n:return 0
        if dp[ind][buy]!=-1:return dp[ind][buy]
        if buy:
            profit = max(-prices[ind]+self.buysell(prices,ind+1,0,n,dp),0+self.buysell(prices,ind+1,1,n,dp))
        else:
            profit = max(prices[ind]+self.buysell(prices,ind+1,1,n,dp),0+self.buysell(prices,ind+1,0,n,dp))
        dp[ind][buy]=profit
    #     print(dp)
        return dp[ind][buy]
    # prices = [7,1,5,3,6,4]
    
    # print(dp)
    # buysell(prices,0,1,len(prices),dp)
        
