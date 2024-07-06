class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # index=0
        t=time%(n-1)
        time-=t
        if (time//(n-1))%2==0:
            return 1+t
        else:
            return n-t
     
                
