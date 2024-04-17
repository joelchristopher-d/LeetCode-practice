class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # """
        # if len(nums)==1:
        #     return nums[0]
        # low=0
        # high=len(nums)-1
        # t=-10**13
        # while(low!=len(nums)):
        #     if low>high:
        #         low+=1
        #         high=len(nums)-1
        #     else:
        #         a=[nums[i] for i in range(low,high+1)]
        # #         print(a,sum(a))
        #         if t<sum(a):
        #             t=sum(a)
        #         high-=1
        # return t
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
