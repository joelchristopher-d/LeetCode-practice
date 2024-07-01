class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        con=0
        for i in arr:
            if con==3:
                return True
            if i%2!=0:
                con+=1
            else:
                con=0
        return True if con==3 else False
