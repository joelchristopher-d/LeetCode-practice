class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        # print(nums)
        k=1
        for i in [j for j in nums if j>0]:
            if i!=k:
                return(k)
            else:
                k+=1
        return k
        #--------------------------------
        # n=[]
        # for i in nums:
        #     if i not in n and i>0 and i<len(nums):
        #         n.append(i)
        # nums=sorted(n)
        # # nums = sorted(nums)
        # for i in range(len(nums)):
        #     if nums[i]!=i+1:
        #         return(i+1)

        # return len(nums)+1
        #-------------------------
        n=len(nums)
        for i in range(n):
#             print(nums[nums[i]-1],n)
            while 0<nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
#         print(nums)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

        
