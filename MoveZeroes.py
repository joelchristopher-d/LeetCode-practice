class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        high=1
        while(high<n):
            if nums[low]!=0:
                low+=1
                high+=1
            else:
                while high<n and nums[high]==0:
                    high+=1
                if high<n:nums[low],nums[high]=nums[high],nums[low]
        
