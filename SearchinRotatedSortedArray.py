class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low=0
        # high=len(nums)-1
        # while(low<high):
        #     mid=(low+high)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>target:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

        
