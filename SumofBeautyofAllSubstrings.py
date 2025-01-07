class Solution:
    def beautySum(self, s: str) -> int:
        l=[]
        for i in range(0,len(s)):
            st = s[i]
            for j in range(i+1,len(s)):
                st+=s[j]
                l.append(st)        
        # print(l)
        total=0
        for i in l:
            total+=self.maximin(i)
        return total

    def maximin(self,substr):
        if len(substr)<=1:return 0
        d={}
        for i in substr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if max(d)!=min(d):
    #         print(substr,max(d.values())-min(d.values()))
            return max(d.values())-min(d.values())
        return 0
            
