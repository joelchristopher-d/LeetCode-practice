class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        a=0
        for i in range(len(heights)):
            if x[i]!=heights[i]:
                a+=1
        return a
