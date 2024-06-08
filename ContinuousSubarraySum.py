class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = {0:-1} 
        res = 0
        for i,n in enumerate(nums):
            res+=n
            # print(res)
            diff = res % k 
            # print(diff)
            if diff not in hm:
                hm[diff] = i
            elif i - hm[diff] > 1:
                return True
        
        return False
