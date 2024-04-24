class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[True if (extraCandies+i >= max(candies)) else False for i in candies]
        return l
