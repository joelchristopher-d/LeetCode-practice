class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0]=1
        for j in range(1,len(t)+1):
            dp[0][j]=0
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):        
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]


        dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        return self.distsubseq2(s,t,len(s)-1,len(t)-1,dp)
        return self.distsubseq(0,s,t,len(s),[])

    def distsubseq(self,ind,s,t,n,l):
        if ind == n:
            if "".join(l) == t:
                return 1
            else:
                return 0
        l.append(s[ind])
        left = self.distsubseq(ind+1,s,t,n,l)
        l.pop()
        right = self.distsubseq(ind+1,s,t,n,l)
        return left + right

    def distsubseq2(self,s,t,i,j,dp):
        if j<0:
            return 1
        if i<0:
            return 0
        if dp[i][j]!=-1: return dp[i][j]
            
        if s[i]==t[j]:
            dp[i][j] = self.distsubseq2(s,t,i-1,j-1,dp) + self.distsubseq2(s,t,i-1,j,dp)
            return dp[i][j]
        dp[i][j] = self.distsubseq2(s,t,i-1,j,dp)
        return dp[i][j]
    
