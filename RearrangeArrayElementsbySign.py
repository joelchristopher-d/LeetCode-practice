class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        low = 0
        high = 0
        while(low<len(nums) and high<len(nums)):
            while nums[low]<0:
                low+=1
            if low<len(nums):
        #         print("low:",low)
                res.append(nums[low])
                low+=1
            while nums[high]>=0:
                high+=1
            if high<len(nums):
        #         print("high:",high)
                res.append(nums[high])
                high+=1
        return res




        pos = []
        neg = []
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        res=[]
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
        
