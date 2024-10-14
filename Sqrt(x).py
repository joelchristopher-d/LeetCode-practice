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


n = 36
def square(n):
    low = 0
    high = n
    while(low<=high):
        mid = (low+high)//2
        print(low,high,mid)
        if mid*mid == n:return mid
        if mid*mid > n:
            high = mid-1
        else:
            low = mid+1
    return high
square(10)
