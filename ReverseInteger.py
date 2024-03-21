class Solution:
    def reverse(self, x: int) -> int:
        l=0
        i=abs(x)
        while(i):
            l=(l*10)+i%10
            i//=10
            
        if l < -2**31 or l > 2**31 - 1:
            return 0    
        if x<0:
            return(-abs(l))
        else:
            return(l)
