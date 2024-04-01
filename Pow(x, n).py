class Solution:
    def myPow(self, x: float, n: int) -> float:
        # def rec(x,n):
        #     if n==0:
        #         return 1
        #     elif n>0:
        #         n-=1
        #         return x*rec(x,n)
        #     else:
        #         n+=1
        #         return 1/x*rec(x,n)


        return (float("{:.5f}".format(x**n)) )
