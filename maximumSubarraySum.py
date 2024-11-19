class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        low = 0
        high = k-1
        res=0
        while(high<len(nums)):
            temp = nums[low:high+1]
            if len(temp)==len(set(temp)):
                res = max(res,sum(temp))
            low+=1
            high+=1
        return res


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        current_sum = 0
        max_sum = 0
        begin = 0

        for end in range(n): 
            if nums[end] not in elements:
                current_sum += nums[end]
                elements.add(nums[end])

                if end - begin + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
                
                begin += 1

        return max_sum
