class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]==target:
                return mid    

            else:
                high = mid-1
        return mid+1 if nums[mid]<target else mid
