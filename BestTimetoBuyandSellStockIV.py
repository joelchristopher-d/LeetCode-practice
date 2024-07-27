class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cap=k
        dp=[[[0 for i in range(cap+1)] for j in range(2)] for k in range(len(prices)+1)]
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(0,2,1):
                for k in range(1,cap+1,1):
                    if buy:
                        dp[ind][buy][k] = max(-prices[ind]+dp[ind+1][0][k],0+dp[ind+1][1][k])
                    else:
                        dp[ind][buy][k] = max(prices[ind]+dp[ind+1][1][k-1],0+dp[ind+1][0][k])
        return dp[0][1][k]
        
