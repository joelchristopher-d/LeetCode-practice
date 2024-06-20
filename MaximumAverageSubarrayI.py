
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k





















class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return sum(nums)/k
        low=0
        high=k
        su=float('-inf')
        while(high<=len(nums)):
        #     print(nums[low:high])
            su= sum(nums[low:high]) if su<sum(nums[low:high]) else su
            low+=1
            high+=1
        return(su/k)
        
