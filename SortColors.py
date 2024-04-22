class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
#     print(l[i])
            for j in range(len(nums)-1-i):
                # print(l[j],end="")
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        return nums
    #     break
        
