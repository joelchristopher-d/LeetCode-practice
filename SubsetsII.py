class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            l1=[]
            for j in res:
                l1.append(sorted([i]+j))
        #         print(l1)
            for k in l1:
                if k not in res:
                    res+=[k]
        return res

        
