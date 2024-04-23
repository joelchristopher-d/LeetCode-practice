class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s)==1:
        #     return s[0]
        # low=0
        # high=len(s)-1
        # t=""
        # while(low<len(s)-1):
        #     a=s[low:high+2]
        # #     print(a,"-",a[::-1])
        #     if low==high:
        #         low+=1
        #         high=len(s)-1
        #     if a==a[::-1] and len(t)<len(a):
        #         t=a 
        #         # break
        #     high-=1
        # return t if t!="" else s[0] 
        p=''
        for i in range(len(s)):
            p1=self.getpal(s,i,i+1)
            p2=self.getpal(s,i,i)
            p=max([p,p1,p2],key=lambda x:len(x))
        return p

    def getpal(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
