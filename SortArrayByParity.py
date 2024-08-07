class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1
        while(low<high):
            while nums[low]%2==0 and low<high:
                low+=1
            while nums[high]%2!=0 and high>low:
                high-=1
            if nums[low]%2!=0 and nums[high]%2==0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1
        return nums
