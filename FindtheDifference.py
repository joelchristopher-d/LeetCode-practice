class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1=sum2=0
        for i in s:
            sum1+=ord(i)
        for i in t:
            sum2+=ord(i)
        return chr(sum2-sum1)



        s=sorted(s)
        t=sorted(t)
        i=0
        while len(s)>i and len(t)>i:
            # print(t[i],s[i])
            if t[i]!=s[i]:
                return t[i]
            i+=1
        return t[-1]
        
