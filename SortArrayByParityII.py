class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        low=0
        high=1
        while(high<len(nums)):
            # print(low,nums)
            while low<len(nums) and nums[low]%2==0:
        #         print(low)
                low+=2
            while high<len(nums) and nums[high]%2!=0:
                high+=2
            if (low<len(nums) and high<len(nums)) and nums[low]%2!=0 and nums[high]%2==0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=2
                high+=2
        return nums
