class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index




        # low=0
        # high=len(nums)-1
        
        # while(low<high):
        #     if nums[low]!=val:
        #         low+=1
        #     elif nums[low]==val:
        #         nums[low],nums[high]=nums[high],nums[low]
        #         high-=1

        # a = [i for i in nums if i!=val]
        # return len(a)
      
