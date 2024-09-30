class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        mpp ={}
        preSum = 0
        cnt = 0
        # mpp[0] = 1
        for i in range(n):
            preSum += nums[i]
            if preSum == k:cnt+=1
            remove = preSum - k
            if remove in mpp:
                cnt+=mpp[remove]
            if preSum not in mpp:mpp[preSum]=1
            else:mpp[preSum]+=1
        return cnt
