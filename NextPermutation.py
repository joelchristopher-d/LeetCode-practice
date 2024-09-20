class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                j = i
                break
        if j == -1:
            self.rev(nums,0,n-1)
        else:
            for i in range(n-1,-1,-1):
                if nums[j]<nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
                    break
            self.rev(nums,j+1,n-1)
    def rev(self,nums,low,high):
        while(low<=high):
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1
        return nums
