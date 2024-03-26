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
       
