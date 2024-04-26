class Solution:
    def tribonacci(self, n: int) -> int:
        # if n==0:
        #     return 0
        # elif n==1 or n==2:
        #     return 1
        # return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        if n<=2:
            return n if n==0 else 1
        a,b,c=0,1,1

        for i in range(3,n+1):
            d=a+b+c
            a,b,c=b,c,d
        return d
