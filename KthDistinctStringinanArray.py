class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l={}
        for i in arr:
            if i in l:
                l[i]+=1
            else:
                l[i]=1

        for i in l:
            if l[i]==1:
                k-=1
            if k==0:
                return i
        return ""
        
        
