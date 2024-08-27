class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.perm(nums)

    def perm(self,nums):
        if len(nums)==0:
            return [[]]
        
        perms = self.perm(nums[1:])
        res = []
        for i in perms:
            for j in range(len(nums)):
                p = i.copy()
                p.insert(j,nums[0])
                res.append(p)
        return res
        
