class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.hour(piles,h)

    def find(self,arr,mid):
        banana = 0
        for i in arr:
            if i<mid:
                banana+=1
            elif i%mid==0:
                banana+=(i//mid)
            else:
                banana+=(i//mid)+1
        return banana



    def hour(self,a,h):
        low = 1
        high = max(a)
        while(low<=high):
            hour = 0
            mid = (low+high)//2
            banana = self.find(a,mid)
            if banana > h:low = mid+1
            else:high = mid-1
        return low
