class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxi=0
        for i in s:
            if i == "(":
                counter+=1
            elif i == ")":
                counter-=1
            maxi = max(maxi,counter)
        return maxi
        
