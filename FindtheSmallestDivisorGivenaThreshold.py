class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while(low<=high):
            mid = (low+high)//2
            eq = self.equate(nums,mid)
            if eq > threshold:
                low = mid+1
            else:
                high = mid-1
        return low





    def equate(self,arr,mid):
        s=0
        for i in arr:
            if i%mid!=0:
                s += (i//mid) + 1
            else:s += (i//mid)
        return s
        
