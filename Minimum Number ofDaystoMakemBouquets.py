class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while(low<=high):
            mid = (low+high)//2
            total = self.mob(bloomDay,mid,k)
            if total<m:
                low = mid+1
            else:
                high = mid-1
        return low
    def mob(self,arr,day,num):
        boq = 0
        total = 0
        for i in arr:
            if i<=day:
                boq+=1
            else:
                total += boq//num
                boq=0
        total += boq//num
        return total
