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



def perm(nums,ds,mapp,res):
    if len(ds)==len(nums):
        res.append(list(ds))
        return
    
    for i in range(len(nums)):
        if mapp[i]==False:
            mapp[i]=True
            ds.append(nums[i])
            perm(nums,ds,mapp,res)
            ds.pop()
            mapp[i]=False
            

nums = [1,2,3]
res=[]
perm(nums,[],[False,False,False],res)
print(res)
        
