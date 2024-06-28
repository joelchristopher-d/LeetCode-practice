class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        l=[0]*n
        for i in roads:
            j,k=i
            l[j]+=1
            l[k]+=1
        # print(l)
        label = 1
        res=0
        for i in sorted(l):
            res+=label*i
        #     print(res)
            label+=1
        return res
                
