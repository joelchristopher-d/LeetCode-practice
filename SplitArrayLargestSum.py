class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while(low<=high):
            mid = (low+high)//2
            if self.cansplit(nums,mid)>k:
                low = mid+1
            else:
                high = mid-1
        return low
    
    
    
    def cansplit(self,arr,size):
        parts = 1
        total = 0
        for i in arr:
            if total + i <=size:
                total+=i
            else:
                total = i
                parts+=1
        return parts
        
