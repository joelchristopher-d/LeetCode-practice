class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        t1={}
        for i in arr:
            t1[i]=0
        for i in arr:
            t1[i]+=1
        # print(t1)
        for i in t1:
            for j in t1:
                if t1[i]==t1[j] and i!=j:
                    return False
        return True
            
