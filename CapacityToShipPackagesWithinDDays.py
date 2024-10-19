class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low<=high):
            mid = (low+high)//2
            MinDay = self.minday(weights,mid)
            if MinDay <= days:
                high = mid-1
            else:
                low = mid+1
        return low
    def minday(self,weights,day):
        temp = day
        find = 1
        for i in range(len(weights)-1):
            temp -= weights[i]
            if temp < weights[i+1]:
                find+=1
                temp = day
        return find
        
