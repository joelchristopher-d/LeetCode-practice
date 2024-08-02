class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1 for i in range(len(s)+1)] for j in range(len(p)+1)]
        return self.match(s,p,len(s)-1,len(p)-1,dp)

    def match(self,s,p,l,r,dp):
    
        if l<0 and r<0:
            return True
        if r<0 and l>=0:
            return False
        if l<0 and r>=0:
            for i in range(r+1):
                if p[i]!="*":
                    return False
            return True
        if dp[r][l]!=-1:return dp[r][l]
        if s[l]==p[r] or p[r]=="?":
            dp[r][l]= self.match(s,p,l-1,r-1,dp)
            return dp[r][l]
        if p[r]=="*":
            dp[r][l]=self.match(s,p,l,r-1,dp) or self.match(s,p,l-1,r,dp)
            return dp[r][l]
        dp[r][l]=False
        return dp[r][l]
            
