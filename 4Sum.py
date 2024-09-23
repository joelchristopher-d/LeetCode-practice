class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = nums[i]+nums[j]
                low = j+1
                high =len(nums)-1
                while(low<high):
                    if temp+nums[low]+nums[high]==target:
                        if sorted([nums[i],nums[j],nums[low],nums[high]]) not in arr:
                            arr.append(sorted([nums[i],nums[j],nums[low],nums[high]]))
                        low+=1
                        high-=1
                    if temp+nums[low]+nums[high]>target:
                        high-=1
                    if temp+nums[low]+nums[high]<target:
                        low+=1
        return arr
