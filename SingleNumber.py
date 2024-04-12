class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        op = nums[0]
        for i in range(1, len(nums)):
            op = op ^ nums[i]
        return op
                
