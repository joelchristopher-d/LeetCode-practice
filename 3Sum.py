class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i+1
            high = len(nums)-1
            
            while(low<high):
                if nums[i]+nums[low]+nums[high]==0:
                    # if [nums[i],nums[low],nums[high]] not in l:
                    l.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low+=1
                    high-=1
                elif nums[i]+nums[low]+nums[high]>0:
                    high-=1
                elif nums[i]+nums[low]+nums[high]<0:
                    low+=1
        return l
