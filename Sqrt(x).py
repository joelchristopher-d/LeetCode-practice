class Solution:
    def mySqrt(self, x: int) -> int:
        # i=0
        # while(i*i <= x):
        #     i+=1
        # return i-1
        b = x
        while b*b > x:
            b = (b+x//b)//2
        return b
