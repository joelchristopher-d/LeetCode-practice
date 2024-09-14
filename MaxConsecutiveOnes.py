class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        frq = 0
        temp = 0
        for i in nums:
            if i==1:
                temp+=1
            else:
                temp=0
            frq = max(frq,temp)
        return frq
