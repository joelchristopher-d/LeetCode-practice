class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        low=0
        high=2*10**9
        while(low<high):
            mid=(low+high)//2
            count = mid//a + mid//b + mid//c - mid//self.lcm(a,b) - mid//self.lcm(b,c) - mid//self.lcm(a,c) + mid//self.lcm(self.lcm(a,b),c)
            if count>=n:
                high = mid
            else:
                low=mid+1
        return low

    def gcd(self,x,y):
        while y:
            x,y=y,x%y
        return x

    def lcm(self,a,b):
        return a*b//self.gcd(a,b) 
