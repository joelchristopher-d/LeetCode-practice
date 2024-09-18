class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = res = total = 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res







        nums.sort()
        max_freq = 0

        for i in range(len(nums) - 1, -1, -1):
            curr_freq = 1
            new_k = k
            curr_ele = nums[i]

            for j in range(i - 1, -1, -1):
                if curr_ele - nums[j] <= new_k:
                    curr_freq += 1
                    new_k -= (curr_ele - nums[j])
                    print(nums[i],nums[j],curr_freq)
                else:
                    break

            max_freq = max(max_freq, curr_freq)
    #         if max_freq== 73:print(nums[i])
            if max_freq >= i:
                break

        return max_freq
            
