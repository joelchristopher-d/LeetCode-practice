class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        a=0
        odd = False
        for i in d:
            if d[i]%2==0:
                a+=d[i]
            else:
                a+=(d[i]-1)
                odd=True
        if odd:
            a+=1
        return a
                        
