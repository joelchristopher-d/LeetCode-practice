def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    low = 0
    high = len(nums)-1
    nums_ = sorted(nums)
    while(low<high):
        if nums_[low]+nums_[high]==target:
            return [nums.index(nums_[low]),nums.index(nums_[high])]
        elif nums_[low]+nums_[high]>target:
            high-=1
        elif nums_[low]+nums_[high]<target:
            low+=1
            
            
            
            
twoSum([3,2,4],6)
