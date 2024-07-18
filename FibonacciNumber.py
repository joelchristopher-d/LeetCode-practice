# DYNAMIC PROGRAMMING

# tabulation technique
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.DP(n)

    def DP(self,n):
        prev1=1
        prev2=0
        for i in range(n-1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1

# memoization
def memoization(n,dp):
    
    if n<=1:return n
    if dp[n]!=-1:return dp[n]
    dp[n] = memoization(n-1,dp) + memoization(n-2,dp)
    return dp[n]

dp=[-1 for i in range(7+1)]
memoization(7,l)

        
