class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        low = -1
        high = len(nums)-1
        for i in range(len(nums)):
            low += 1
            high = len(nums)-1
            while(low<high):
                if nums[low]==nums[high]:
                    nums.pop(high)
                high-=1
        return len(nums)



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low=0
        high=low+1
        while(high<len(nums)):
            if nums[low]==nums[high]:
                high+=1
            else:
                nums[low+1]=nums[high]
                low+=1
                high+=1
        return low+1
       
       
